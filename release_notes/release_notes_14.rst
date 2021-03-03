:author: Charles Callaway
:date: 02-03-2021
:modified: 02-03-2021
:tags: release notes
:lang: en-US
:translation: false
:status: completed

.. include:: ../sphinx-roles.txt


.. _release_notes_v1_4:

=======================
Version 1.4.1 (Current)
=======================

Alyvix Server is a software tool for scaling up the management of instances of the Alyvix
visual monitoring system.

.. _release_notes_v1_4_1:

.. topic:: Alyvix Server Version 1.4.1

   **Release date:**  March 2nd, 2021

**New Features**

* You can set a :ref:`waiting period between workflows <test_case_flow_assignment>`
  (measured in minutes)
* You can set a :ref:`waiting period between test cases <test_case_flow_assignment>`
  (measured in minutes)
* The sequence of execution of declared test cases
  :ref:`are now sortable <session_management_test_cases>`
* The workflows panel now shows the :ref:`overall control table <test_case_flow_assignment>`
  with the sorted test cases and which session they are enabled in

**Improvements**

* The previous workflow execution sequences are now flushed and cleaned
  when clicking the break or stop buttons
* The traffic light icons for sessions are now only red when the Alyvix bot
  is actually operating in a session, and light green during waiting periods

**Frontend Control Panels**

The endpoint URLs are now as follows:

* :file:`<alyvix_server>/`
* :file:`<alyvix_server>/testcases`
* :file:`<alyvix_server>/settings`
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

