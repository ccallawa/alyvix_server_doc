:author: Charles Callaway
:date: 22-09-2020
:modified: 29-09-2020
:tags: index
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt



.. _transaction_reporting_top:

=====================
Transaction Reporting
=====================

.. todo::

   Introductory paragraph (explanation, relation to other elements)

The Report Listing endpoint displays a list of all recent runs of a given test case alias in
reverse chronological order.  It contains the following information for each run:

* **Timestamp:**  The moment when that test case was launched, internally expressed as a Unix Epoch
* **Runcode:**  A unique code that identifies a particular run of a particular alisas on a particular host
* **Host:**  The virtual machine that the test case was run on
* **User:**  The username under which the session was opened

The following endpoint will produce the report listing in HTML format in a browser:

.. table::
   :class: tablecell-endpoint

   +--------------------------------------------------------------------------------+
   | Report Listing Endpoint                                                        |
   +-----------+--------------------------------------------------------------------+
   | Endpoint: | :bolditalic:`http://<IP Address>/<API>/testcases/<alias>/reports`  |
   +-----------+--------------------------------------------------------------------+
   | Example:  | :bolditalic:`http://localhost/v0/testcases/shipping_w1/reports`    |
   +-----------+--------------------------------------------------------------------+

The reports page contains a fixed number of rows, which can be advanced by using the controls
at the bottom.  All reports are available until they have passed
:ref:`the retention period set <session_management_settings>` for the session under which
they launched (remember that you can set the retention period separately for successful versus
failed runs).

Each row contains a link to the detailed report which is indexed by the runcode.  Rows marked in
red indicate test cases that failed.  To obtain the detailed report of a specific run, you can
either click on the link, or use the Report Details endpoint directly by inserting the *runcode*
into the endpoint URL:

.. table::
   :class: tablecell-endpoint
   :widths: 5 95

   +-------------------------------------------------------------------------------------------------------------+
   | Report Details Endpoint                                                                                     |
   +-----------+-------------------------------------------------------------------------------------------------+
   | Endpoint: |:bolditalic:`http://<IP Address>/<API>/testcases/<alias>/reports/?runcode=<runcode>`             |
   +-----------+-------------------------------------------------------------------------------------------------+
   | Example:  | :bolditalic:`http://localhost/v0/testcases/shipping_w1/reports/?runcode=pb01Al01vino1601287294` |
   +-----------+-------------------------------------------------------------------------------------------------+



.. todo::

   Need some description of a report, but without too much detail.  Say it's easy to see the screenshots.



.. code-block::

   visittrentino report
   Date: 2020/09/18 11:49:17.790 UTC+0200, runcode: pb01Al01vino1600422555, hostname: pbzalyvixts01, username: WP\AlyvixUser01
   Testcase name: visittrentino, testcase args: None, testcase alias: visittrentino, duration: 8949 ms
   Resolution width: 1280, Resolution height: 800, scaling factor: 100%

   Timestamp: 2020/09/18 11:49:17.790 UTC+0200, name: vt_home_ready, alias: vt_home_ready, group: None
   Detection type: appear, timeout: 10000 ms, warning: None ms, critical: None ms
   Performance: 2849 ms, accuracy: 61 ms, exit: true
   Record text: , record extract:
   Transaction Screenshot:   <screenshot>

|
