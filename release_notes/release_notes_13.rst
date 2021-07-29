:author: Charles Callaway
:date: 03-12-2020
:modified: 03-12-2020
:tags: release notes
:lang: en-US
:translation: false
:status: completed

.. include:: ../sphinx-roles.txt



.. _release_notes_v1_3:

=============================
Version 1.3.0 - Version 1.3.1
=============================

Alyvix Server is a software tool for scaling up the management of instances of the Alyvix
visual monitoring system.

.. _release_notes_v1_3_1:

.. rubric:: Alyvix Server Version 1.3.1

**Release date:**  December 14th, 2020

**Bug fixes**

* Alyvix Server now allows setting session passwords that contain special characters

**Frontend Control Panels**

The following endpoint URLs are now:

* :file:`<alyvix_server>/workflows`

  * :file:`<alyvix_server>/workflow?username=<domain\username>`

* :file:`<alyvix_server>/testcases`
* :file:`<alyvix_server>/settings (or just <alyvix_server>/)`
* :file:`<alyvix_server>/nats-influxdb`

**Measurement Web APIs (v0)**

The following endpoint URLs remain:

* :file:`<alyvix_server>/v0/testcases`

  * :file:`<alyvix_server>/v0/testcases/<testcasealias>`

    * :file:`<alyvix_server>/v0/testcases/<testcasealias>?screenshots=[true, false]`

  * :file:`<alyvix_server>/v0/testcases/<testcasealias>/reports`

    * :file:`<alyvix_server>/v0/testcases/<testcasealias>/reports?runcode=<runcode>`

* :file:`<alyvix_server>/v0/flows/run?username=<domain\username>`



.. _release_notes_v1_3_0:

.. rubric:: Alyvix Server Version 1.3.0

**Release date:**  December 3rd, 2020

**New Features**

* Alyvix Server can now :ref:`stream measurements <session_management_nats>`
  through multi-tenant NATS/InfluxDB TLS channels

**Improvements**

* Alyvix Server shows an improved UI of control and report panels

**Frontend Control Panels**

The following endpoint URLs are now:

* :file:`<alyvix_server>/workflows`

  * :file:`<alyvix_server>/workflow?username=<domain\username>`

* :file:`<alyvix_server>/testcases`
* :file:`<alyvix_server>/settings` |halftab| (or just :file:`<alyvix_server>/`)
* :file:`<alyvix_server>/nats-influxdb`

**Measurement Web APIs (v0)**

The following endpoint URLs remain:

* :file:`<alyvix_server>/v0/testcases`

  * :file:`<alyvix_server>/v0/testcases/<testcasealias>`

    * :file:`<alyvix_server>/v0/testcases/<testcasealias>?screenshots=[true, false]`

  * :file:`<alyvix_server>/v0/testcases/<testcasealias>/reports`

    * :file:`<alyvix_server>/v0/testcases/<testcasealias>/reports?runcode=<runcode>`

* :file:`<alyvix_server>/v0/flows/run?username=<domain\username>`

|
