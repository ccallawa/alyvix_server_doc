:author: Charles Callaway
:date: 22-09-2020
:modified: 29-09-2020
:tags: index
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt



.. _test_case_scheduling_top:

====================
Test Case Scheduling
====================

.. todo::

   Introductory paragraph (explanation, relation to other elements)

Alyvix Server provides a basic scheduler that takes the workflows you have configured, and starts
them at regular intervals on the sessions you assigned them to.  There are three main concepts
to understand:

* **Session Workflows:**  A *flow* is a set of Alyvix test cases that are assigned to a session,
  drawn from the available test cases in the global configured
  :ref:`Test Case Path <session_management_settings>`.
* **Scheduling Period:**  The length of time in seconds until Alyvix Server will restart the
  *flow* assigned to a particular session.  Once all of the test cases in the *flow* have
  completed, no further test cases will be run on that session until the current scheduling
  period finishes.
* **Session State:**  An Alyvix Server session is either:

  * **Running:**  A test case is currently running in the configured session
  * **Waiting:**  All test cases have been completed within this *scheduling period*
  * **Stopped:**  The scheduler is not running and will not initiate a new *flow*

You can control how Server transitions between these states with the controls described below.



.. _test_case_flow_management:

*************************
Test Case Flow Management
*************************

.. todo::

   Introductory paragraph (explanation, relation to other elements)

.. table::
   :class: tablecell-endpoint

   +-----------------------------------------------------+
   | Flow Management Endpoint                            |
   +-----------+-----------------------------------------+
   | Endpoint: | :bolditalic:`http://<IP Address>/flows` |
   +-----------+-----------------------------------------+
   | Example:  | :bolditalic:`http://localhost/flows`    |
   +-----------+-----------------------------------------+

.. table::
   :class: tablecell-endpoint

   +--------------------------------------------------------------------------------+
   | Flow Management Endpoint                                                       |
   +-----------+--------------------------------------------------------------------+
   | Endpoint: | :bolditalic:`http://<IP address>/flow?username=<domain\\username>` |
   +-----------+--------------------------------------------------------------------+
   | Example:  | :bolditalic:`http://localhost/flows?username=MS\\johnsmith`        |
   +-----------+--------------------------------------------------------------------+

The Flow interface is organized by session, with one session per row.  The main components are:

* **Username:**  The name of the session, as defined on the
  :ref:`session management page <session_management_session_description>`
* **Flow:**  The sequence of Alyvix test cases that the scheduler should run on a given session.
  You can change which test case aliases are included in a given flow by clicking on the
  "Open Flow" action.
* **Flow state:**  How that flow is currently executing (running or not running)
* **Session state:**  How the session is set to progress, as managed by the user

You can manage the session state with the following actions:

* **Run:**  Start the session using the scheduler, which will automatically execute the session's
  assigned flow
* **Break:**  Force the currently running test case of a session to immediately proceed to its
  fail/exit section, then halt the scheduler until further action is taken
* **Stop:**  Force the currently running test case of a session to immediately stop without running
  either its fail or exit sections, then halt the scheduler until further action is taken
* **Manual:**  Stop the scheduler after the next test case has completed, then permit manual
  scheduling where a custom endpoint URL that includes a test case alias is inserted into the
  browser's address bar.  Automated scheduling can be restarted with the *Run* action.

Once the scheduler has stopped, you can use the following endpoint to manually run a session,
where the domain and user names indicate which session to run one time:

.. table::
   :class: tablecell-endpoint

   +------------------------------------------------------------------------------------------+
   | Manual Scheduling Endpoint                                                               |
   +-----------+------------------------------------------------------------------------------+
   | Endpoint: | :bolditalic:`http://<IP address>/v0/flows/run?username=<domain>\\<username>` |
   +-----------+------------------------------------------------------------------------------+
   | Example:  | :bolditalic:`http://localhost/v0/flows/run?username=MS\\johnsmith`           |
   +-----------+------------------------------------------------------------------------------+

|

