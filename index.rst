:author: Charles Callaway
:date: 22-09-2020
:modified: 02-11-2020
:tags: index
:lang: en-US
:translation: false
:status: final

.. include:: sphinx-roles.txt


.. toctree::
   :maxdepth: 2
   :name: toc_master
   :hidden:

   install.rst
   session_management.rst
   test_case_scheduling.rst
   measurement_web_apis.rst
   transaction_reporting.rst
   release_notes.rst
   Alyvix User Manual <https://alyvix.com/learn/>
   get_in_touch.rst

|



.. _home:

#############
Alyvix Server
#############

Welcome to the official guide for **Alyvix Server 1.3**.

`Alyvix <https://alyvix.com/>`_ lets you build end-user bots that visually interact with any
Windows application like ERPs, or any web app in your favorite browser.

**Alyvix Server** lets you scale up visual monitoring by managing all of your tests at a single
point.  You can schedule end-user bots continuously and in parallel, while keeping your Windows
RDP sessions up and running.  It helps you report end-user experiences by retrieving the test case
measurements and screenshots, as well as looking directly at their summary reports.

Alyvix Server provides the following features:

* **Session Management:**   Keeps multiple Windows Server sessions alive
* **Test Case Scheduling:**  Runs test cases continuously and in parallel
* **Measurement Web APIs:**  Provides recorded measurements and screenshots on demand
* **Transaction Reporting:**  Helps you find and view the certified results for each test case run

Alyvix Server runs on Windows, opening multiple, independent sessions on a private network.  On
each session it schedules monitoring test cases, collects their measurements, and logs the sets of
Alyvix test cases you select.  Everything from configuration to reporting is managed by a set of
RESTful endpoints, so you can access any part of Alyvix Server in your browser, from anywhere in
the world.

In addition to the terminology used with Alyvix Editor and Robot, Alyvix Server adds the
following concepts:

* **Session:**  A two-way connection between Alyvix Server and a target Windows session
  that allows Alyvix Server to run test cases and gather metrics from that target session
* **Scheduling:**  A process that ensures that multiple Alyvix test cases are run at set intervals
  on the proper sessions
* **Alias:**  A unique identifier that combines a specific test case with a specific set of
  arguments, allowing you to distinguish between multiple versions of a single test case across
  sessions
* **Flow:**  The set of Alyvix test cases that are planned for execution on a particular session
* **Runcode:**  A code that uniquely identifies a particular test case run by Alyvix Robot
* **Report:**  A human-readable document that shows concrete proof of how a specific test case run
  performed, supported with screenshots

Together, the Alyvix suite of monitoring applications lets you guarantee to yourself or your
clients that both native applications and web apps are functioning properly, no matter how many
servers you manage.
