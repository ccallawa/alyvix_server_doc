:author: Charles Callaway
:date: 20-01-2022
:modified: 20-01-2022
:tags: release notes
:lang: en-US
:translation: false
:status: completed

.. include:: ../sphinx-roles.txt



.. _release_notes_v1_6:

=======================
Version 1.6.0 (Current)
=======================

Alyvix Server is a software tool for scaling up the management of instances of the Alyvix
visual monitoring system.

.. _release_notes_v1_6_0:

.. rubric:: Alyvix Server Version 1.6.0

**Release date:**  January 20th, 2022

**New Features**

* A TLS SMTP connection can be configured in order to receive an email notification about the
  Alyvix Server license expiration date, 1 month in advance

**Improvements**

* Alyvix Server checks only the expiration date (and not the start date) to validate licenses

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
