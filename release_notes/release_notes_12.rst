:author: Charles Callaway
:date: 05-11-2020
:modified: 05-11-2020
:tags: release notes
:lang: en-US
:translation: false
:status: completed

.. include:: ../sphinx-roles.txt



.. _release_notes_v1_2:

=======================
Version 1.2.0 - Current
=======================

Alyvix Server is a software tool for scaling up the management of instances of the Alyvix
visual monitoring system.

The initial release of Alyvix Server v1.1 brings all of the basic functionality necessary
to schedule and run test cases, and retrieve data and reports from those runs.

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
