:author: Charles Callaway
:date: 22-09-2020
:modified: 22-09-2020
:tags: index
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. toctree::
   :maxdepth: 2
   :name: toc_master
   :hidden:

   session_management.rst
   test_case_scheduling.rst
   measurement_web_apis.rst
   transaction_reporting.rst
   release_notes.rst
   get_in_touch.rst

|



.. _home:

############################
Alyvix and Visual Monitoring
############################

Welcome to the official guide for **Alyvix Server 1.0.0**.

`Alyvix <https://alyvix.com/>`_ lets you build end-user bots that visually interact with any
Windows application like ERPs, or any web app in your favorite browser.

Alyvix Server lets you scale up visual monitoring by managing your tests.  You can schedule
end-user bots continuously and in parallel, while keeping your Windows RDP sessions up and running.
It helps you report end-user experiences by retrieving the test case measurements and screenshots,
as well as looking directly at their summary reports.

Alyvix Server has the following features:

* **Session Management:**   Keep multiple Windows Server sessions alive
* **Test Case Scheduling:**  Run your test cases continuously and in parallel
* **Measurement Web APIs:**  Provide recorded measurements and screenshots on demand
* **Transaction Reporting:**  Look at the certified results for each test case run



.. _home_outline:

=======
Outline
=======


* Getting started (network architecture)

  * Installation

* General settings (../server) (machine architecture)
* Test case declaration (../testcases)
* Test case scheduling (../flows) (basic scheduler concepts)
* Test case apis

  * Test case measurements (../v1/testcases/<testcase_alias>)
  * Test case reports (../v1/testcases/<testcase_alias>/reports)



.. _home_what_next:

================
What to Do First
================

The first step is to
