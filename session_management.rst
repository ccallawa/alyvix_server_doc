:author: Charles Callaway
:date: 22-09-2020
:modified: 05-10-2020
:tags: index
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt



.. _session_management_top:

==================
Session Management
==================

A session is the connection between Alyvix Server and the virtual machines, cloud instances, or
physical servers you want to run Alyvix test cases on.  Alyvix Server can manage multiple sessions
for you, even on completely different machines, allowing you to define what you want to achieve
and letting Alyvix Server take care of the details.  That's what we mean by scaling up -- adding
more machines doesn't mean you have to spend more of your time.



.. _session_management_settings:

***************************
Session Management Settings
***************************

Assuming you've already created test cases with Alyvix Editor, when you first use Alyvix Server
you'll need to configure some basic settings.

The session management settings are global parameters governing all Alyvix test case sessions run
on a specific Alyvix Server (that is, a single IP address).  You can view or edit them by going
to the following endpoint in a browser on your private network:

.. table::
   :class: tablecell-endpoint

   +------------------------------------------------------+
   | Session Management Endpoint                          |
   +-----------+------------------------------------------+
   | Endpoint: | :bolditalic:`http://<IP address>/server` |
   +-----------+------------------------------------------+
   | Example:  | :bolditalic:`http://localhost/server`    |
   +-----------+------------------------------------------+

These global test case settings are:

* **Test Case Path:** A Windows-format absolute or relative path
  (e.g., :file:`C:\\Alyvix\\Testcases\\`) that points to a directory containing all of the
  Alyvix 3 test cases that can be run by this instance of Alyvix Server.  If you add or update
  any test cases, or change this path, Alyvix Server will automatically and immediately pick up
  those changes.
* **Private Key:**  A cleartext private key that Alyvix Robot can use to decrypt any encrypted
  keys you have stored in an Alyvix test case when you created it.
* **Scheduling Period [s]:**  The length of time in seconds until Alyvix Server will restart the
  *flow* assigned to a particular session.  The scheduling period is the same across all sessions
  on a given Alyvix Server.
* **Retention Period Success [d]:**  The number of days that successful test case runs will be
  stored and :ref:`available for immediate inspection <transaction_reporting_top>`.
* **Retention Period Failure [d]:**  The number of days that failed test case runs will be
  stored.

.. _session_management_session_description:

To update the values for these settings, go to the endpoint above, enter the new value in the
appropriate field, and press the :guilabel:`Set` button.

The endpoint above also contains the settings for individual sessions:

* **Domain and Username:**  The Windows domain and login name needed to create a session on the
  server with the same IP address as the endpoint.
* **Password:**  The corresponding password.
* **Resolution\@scaling factor:**  The screen resolution and scaling (zoom) factor of the RDC
  window that will host the session.  All test cases in the session's flow should contain test
  case objects that include the resolution and factor set here.

To update the values for these settings, go to the endpoint above, enter the new value in the
appropriate field, and press the :guilabel:`Update` button.  :guilabel:`Remove` will remove an
existing session, while :guilabel:`Add` will insert a new one.



.. _session_management_test_cases:

***************************
Managing Session Test Cases
***************************

Test cases in the :ref:`specified test case directory <session_management_settings>` can be added
to any session on the Alyvix Server containing them.  However, just because a test case is stored
in that directory doesn't mean that it will be scheduled.  It must first be added to the test case
table by configuring it via the following endpoint:

.. table::
   :class: tablecell-endpoint

   +---------------------------------------------------------+
   | Session Test Case Endpoint                              |
   +-----------+---------------------------------------------+
   | Endpoint: | :bolditalic:`http://<IP address>/testcases` |
   +-----------+---------------------------------------------+
   | Example:  | :bolditalic:`http://localhost/testcases`    |
   +-----------+---------------------------------------------+

Each test case can also appear multiple times in the test case table, including with different
arguments to pass to Alyvix Robot.  The first three settings create the schedulable test case
configuration:

* **Name:**  A test case which can be found in the test case directory.
* **Arguments:**  Arguments that can be passed to a *map* in Alyvix Robot, separated by commas.
* **Alias:**  The name of the schedulable test case configuration.  While this can be any string
  you choose (unique with respect to other test case aliases), combining the test case name and
  an argument, or just the test case name alone, can aid understanding of dashboards and reports.

The *screenshot settings* allow you to configure

  * **Screen Recording:**

    * **Any Output:**  Take a screenshot once for each test case object.
    * **Broken Output Only:**  Take a screenshot only when a test case object fails.
    * **None:**  Never take a screenshot.

  * **Screen Compression:**

    * **Lossless:**  Keep the original screenshot without compressing it.
    * **Compressed:**  Compress all screenshots for this schedulable test case configuration.


To remove a test case from the table, go to the endpoint above and press the :guilabel:`Remove`
button.  :guilabel:`Add` will insert a new row at the bottom of the table (you should insert
the values before pressing the :guilabel:`Add` button).

|
