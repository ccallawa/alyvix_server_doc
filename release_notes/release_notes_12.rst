:author: Charles Callaway
:date: 05-11-2020
:modified: 23-11-2020
:tags: release notes
:lang: en-US
:translation: false
:status: completed

.. include:: ../sphinx-roles.txt



.. _release_notes_v1_2:

=======================================
Version 1.2.0 - Version 1.2.1 (Current)
=======================================

Alyvix Server is a software tool for scaling up the management of instances of the Alyvix
visual monitoring system.

.. _release_notes_v1_2_1:

.. topic:: Alyvix Server Version 1.2.1

   **Release date:**  November 23rd, 2020

**Improvements**

* Alyvix Server now updates the existing database tables after installing a new Alyvix Server release

**Bug Fixes**

* Alyvix Server keeps alive RDP sessions after their passwords have been changed
* Alyvix Server will now obscure session passwords that have been saved within the settings panel
* Alyvix Server can now manage session credentials (*i.e.*, <domain>\\<username>) that contain
  characters such as ``.`` and ``-``
* Alyvix Server now schedules test cases with camel-cased names and displays data from their execution
* Alyvix Client now runs as a minimized window in the taskbar
* Alyvix Server didn't retain and display data from test cases that have been manually stopped with
  the break or stop controls (remember to also
  `upgrade Alyvix <https://alyvix.com/learn/getting_started/install.html#upgrading-alyvix>`_
  to fix this!)
* Alyvix Report didn't show links to the Alyvix Server control panels

**Frontend Control Panels**

The following endpoint URLs remain:

* <alyvix_server>/settings (or just <alyvix_server>/)
* <alyvix_server>/testcases
* <alyvix_server>/workflows

  * <alyvix_server>/workflow?username=<domain\username>

**Measurement Web APIs (v0)**

The following endpoint URLs remain:

* <alyvix_server>/v0/testcases

  * <alyvix_server>/v0/testcases/<testcasealias>

    * <alyvix_server>/v0/testcases/<testcasealias>?screenshots=[true, false]

  * <alyvix_server>/v0/testcases/<testcasealias>/reports

    * <alyvix_server>/v0/testcases/<testcasealias>/reports?runcode=<runcode>

* <alyvix_server>/v0/flows/run?username=<domain\username>

|


.. _release_notes_v1_2_0:

.. topic:: Alyvix Server Version 1.2.0

   **Release date:**  November 5th, 2020

**New Features**

* Alyvix Server works through the HTTPS communication protocol
* Alyvix Server shows a new UI of control and report panels

**Frontend Control Panels**

The following endpoint URLs are now:

* <alyvix_server>/settings
* <alyvix_server>/testcases
* <alyvix_server>/workflows

  * <alyvix_server>/workflow?username=<domain\username>

**Measurement Web APIs (v0)**

The following endpoint URLs remain:

* <alyvix_server>/v0/testcases

  * <alyvix_server>/v0/testcases/<testcasealias>

    * <alyvix_server>/v0/testcases/<testcasealias>?screenshots=[true, false]

  * <alyvix_server>/v0/testcases/<testcasealias>/reports

    * <alyvix_server>/v0/testcases/<testcasealias>/reports?runcode=<runcode>

* <alyvix_server>/v0/flows/run?username=<domain\username>

|
