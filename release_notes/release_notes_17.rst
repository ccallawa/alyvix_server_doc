:author: Charles Callaway
:date: 29-09-2022
:modified: 29-09-2022
:tags: release notes
:lang: en-US
:translation: false
:status: updating

.. include:: ../sphinx-roles.txt



.. _release_notes_v1_7:

=======================
Version 1.7.3 (Current)
=======================

Alyvix Server is a software tool for scaling up the management of instances of the Alyvix
visual monitoring system.

.. _release_notes_v1_7_0:

.. _release_notes_v1_7_3:

.. rubric:: Alyvix Server Version 1.7.3

**Release date:**  September 29th, 2022

**New Features**

* New (deeper) database cleaning logic based on data (measures and images) retention periods
  of successful and failed test cases
* New image recording logic based on successful (no images by default) and failed test cases
  (screenshot, annotation and definition images for each transaction)
* New visual recording in reports, especially visual definition images for each transaction

**Improvements**

* New report format

**Frontend Control Panels**

The following endpoint URLs remain unchanged:

* :file:`<alyvix_server>/`
* :file:`<alyvix_server>/activation`
* :file:`<alyvix_server>/settings`
* :file:`<alyvix_server>/testcases`
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
