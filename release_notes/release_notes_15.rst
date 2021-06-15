:author: Charles Callaway
:date: 14-06-2021
:modified: 14-06-2021
:tags: release notes
:lang: en-US
:translation: false
:status: completed

.. include:: ../sphinx-roles.txt



.. _release_notes_v1_5:

=======================
Version 1.5.0 (Current)
=======================

Alyvix Server is a software tool for scaling up the management of instances of the Alyvix
visual monitoring system.

.. _release_notes_v1_5_0:

.. topic:: Alyvix Server Version 1.5.0

   **Release date:**  June 14th, 2021

**New Features**

* Implementation of a licensing system:

  * Use of a unique instance code for each Alyvix Server machine
  * Through an activation endpoint you can export a license request, import a license file and
    check the enabled features
  * Activation of all Alyvix Server controls based on an importable valid license,
    for a certain number of workflows and during a certain time range

**Improvements**

* When you uninstall Alyvix Server, it removes the Windows service, its software, and its
  scheduled tasks, but retains your certificates (for the TLS web application and the TLS
  data channels), database, and configuration files

**Bug Fixes**

* Browse all the legitimate pages of the report list:  only correct page numbers and their links are shown
* Do not initiate a manual run call if a workflow is already underway
* Save PNG screenshots in reports if you set the screen compression parameter to *lossless*


**Frontend Control Panels**

The following endpoint URL has been added:

* :file:`<alyvix_server>/activation`

The following endpoint URLs remain unchanged:

* :file:`<alyvix_server>/`
* :file:`<alyvix_server>/testcases`
* :file:`<alyvix_server>/settings`
* :file:`<alyvix_server>/nats-influxdb`


**Measurement Web APIs (v0)**

The following endpoint URLs remain unchanged:

* :file:`<alyvix_server>/v0/testcases`

  * :file:`<alyvix_server>/v0/testcases/<testcasealias>`

    * :file:`<alyvix_server>/v0/testcases/<testcasealias>?screenshots=[true, false]`

  * :file:`<alyvix_server>/v0/testcases/<testcasealias>/reports`

    * :file:`<alyvix_server>/v0/testcases/<testcasealias>/reports?runcode=<runcode>`

* :file:`<alyvix_server>/v0/flows/run?username=<domain\username>`

|
