:author: Charles Callaway
:date: 22-09-2020
:modified: 06-10-2020
:tags: release notes
:lang: en-US
:translation: false
:status: final

.. include:: ../sphinx-roles.txt



.. _release_notes_v1_1:

=============
Version 1.1.0
=============

Alyvix Server is a software tool for scaling up the management of instances of the Alyvix
visual monitoring system.

The initial release of Alyvix Server v1.1 brings all of the basic functionality necessary
to schedule and run test cases, and retrieve data and reports from those runs.

.. _release_notes_v1_1_0:

.. topic:: Alyvix Server Version 1.1.0

   **Release date:**  October 6th, 2020

**New Features**


* **Session Management:**  Alyvix Server helps you organize the global parameters like credentials,
  test case paths, and screen resolutions that you need to centrally manage your visual monitoring
  setup.  It keeps all of your Windows Server sessions alive and active, ensuring that your test
  cases can continue to run indefinitely.

* **Test Case Scheduling:**  Test cases are run continuously and in parallel

  * Basic scheduler

    * scheduling period
    * session workflows
    * session run, break and stop controls
    * session manual scheduling control and API

* **Measurement Web APIs:**  Provides recorded measurements and screenshots on demand

  * Test case alias list
  * Test case alias transaction measurements
  * Test case alias transaction screenshots

* **Transaction Reporting:**  Retains certified results and logs for each test case run

  * Retention period for successful runs and for failed ones
  * Test case alias report list
  * Test case alias specific report

* **RESTful Endpoints:** Alyvix supplies endpoint URLs for interfaces and data retrieval:

  * **Frontend Control Panels** allow you to configure parameters and initiate actions
  * **Measurement Web APIs (v0)** return either machine-readable (JSON) or human-readable
    data and reports on demand

|
