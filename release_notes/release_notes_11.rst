:author: Charles Callaway
:date: 22-09-2020
:modified: 22-09-2020
:tags: release notes
:lang: en-US
:translation: false
:status: updating

.. include:: ../sphinx-roles.txt



.. _release_notes_v1_0:

=======================
Version 1.0.0 - Current
=======================

Alyvix Server is a software tool for managing instances of the Alyvix visual monitoring system.


.. _release_notes_v1_0_0:

.. topic:: Version 1.0.0

   **Release date:**  September 30th, 2020

**New Features**

* :ref:`Feature #1 <release_notes_v1_0_0>`:  Description
* :ref:`Feature #2 <release_notes_v1_0_0>`:  Description


New Features

* Session Management

  * User sessions

    * domain\username
    * (clear) password
    * resolution\@scaling factor

  * Test cases

    * centralized path
    * (clear) private key
    * alias map (name/arguments/alias)
    * screenshot settings

* Test Case Scheduling

  * Basic scheduler

    * scheduling period
    * session workflows
    * session run, break and stop controls
    * session manual scheduling control and API

* Measurement Web APIs

  * Test case alias list
  * Test case alias transaction measurements
  * Test case alias transaction screenshots

* Transaction Reporting

  * Retention period for successful runs and for failed ones
  * Test case alias report list
  * Test case alias specific report


Frontend Control Panels

* <alyvix_server>/server
* <alyvix_server>/testcases
* <alyvix_server>/flows

  * <alyvix_server>/flow?username=<domain\username>


Measurement Web APIs (v0)

* <alyvix_server>/v0/testcases

  * <alyvix_server>/v0/testcases/<testcasealias>

    * <alyvix_server>/v0/testcases/<testcasealias>?screenshots=[true, false]

  * <alyvix_server>/v0/testcases/<testcasealias>/reports

    * <alyvix_server>/v0/testcases/<testcasealias>/reports?runcode=<runcode>

* <alyvix_server>/v0/flows/run?username=<domain\username>
