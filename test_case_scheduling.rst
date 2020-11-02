:author: Charles Callaway
:date: 22-09-2020
:modified: 02-11-2020
:tags: index
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt



.. _test_case_scheduling_top:

====================
Test Case Scheduling
====================

Alyvix Server provides a basic scheduler that takes the flows you have configured, and starts
them at regular intervals on the sessions you assigned them to.

There are three main concepts to understand:

* **Session Workflows:**  A *flow* is a set of Alyvix test case aliases that are assigned to a
  session, drawn from the available test case aliases, which in turn are drawn from the test cases
  in the global configured :ref:`Test Case Path <session_management_settings>`.
* **Scheduling Period:**  The length of time in seconds until Alyvix Server will try to run the
  next test case alias of the *flow* assigned to a particular session.  Once all of the test cases
  in the flow have completed, the scheduler will restart that flow from the beginning.
* **Session State:**  An Alyvix Server session can be in one of these two states:

  * **Ready:**  The scheduler is waiting to initiate a new test case alias
  * **Busy:**  A test case alias is currently running in the configured session

.. comment

   You can control how Server transitions between these states with the controls described below.

   .. image:: pictures/server-scheduler.png
      :class: image-boxshadow
      :alt: Alyvix Server Scheduler
      :target: https://youtu.be/rC_bjgXCcZ4

   In the diagram above, the horizontal rows represent the session workflows, the scheduling period
   is the distance between any two of the "flags", and the session state is indicated by the flag
   itself, with red indicating "busy" and green indicating "ready".  A test case is run whenever
   a scheduling period begins (green flag), and at least one test case alias in the workflow has not
   yet run during that period.  :warn:`This doesn't sound right.`



.. _test_case_flow_management:

*************************
Test Case Flow Management
*************************

After you have defined the session and test case configurations, you can begin to assign individual
Alyvix test case aliases to a particular session, and then initiate the execution of test cases.
You can directly determine which aliases will be included via the following endpoint by simply
ticking the checkbox for each alias (within a flow, test case aliases are run in the order they
were entered).

.. table::
   :class: tablecell-endpoint

   +--------------------------------------------------------------------------------+
   | Flow / Test Case Assignment Endpoint                                           |
   +-----------+--------------------------------------------------------------------+
   | Endpoint: | :bolditalic:`http://<IP address>/flow?username=<domain\\username>` |
   +-----------+--------------------------------------------------------------------+
   | Example:  | :bolditalic:`http://localhost/flows?username=MS\\johnsmith`        |
   +-----------+--------------------------------------------------------------------+

Alternatively, you can use the interface in the global flow management endpoint to access each
session flow individually by following the appropriate links:

.. table::
   :class: tablecell-endpoint

   +-----------------------------------------------------+
   | Flow Management Endpoint                            |
   +-----------+-----------------------------------------+
   | Endpoint: | :bolditalic:`http://<IP Address>/flows` |
   +-----------+-----------------------------------------+
   | Example:  | :bolditalic:`http://localhost/flows`    |
   +-----------+-----------------------------------------+

The Flow interface is organized by session, with one session per row.  The main components are:

* **Username:**  The name of the session, as defined on the
  :ref:`session management page <session_management_session_description>`
* **Flow:**  The sequence of Alyvix test case aliases that the scheduler runs on a given
  session.  You can change which test case aliases are included in a given flow by clicking on the
  "Open Flow" action.
* **Flow state:**  How that flow is currently executing (running or not running)
* **Session state:**  How the session is set to progress, as managed by a user action below

.. _test_case_flow_management_actions:

Once a flow has at least one assigned test case alias, it can be scheduled.  You can manage the
session state with the following actions:

* **Run:**  Start the session using the scheduler, which will automatically execute the session's
  assigned flow
* **Break:**  Force the currently running test case of a session to immediately proceed to its
  fail/exit section, then halt the scheduler until further action is taken
* **Stop:**  Force the currently running test case of a session to immediately stop without running
  either its fail or exit sections, then halt the scheduler until further action is taken
* **Manual:**  Stop the scheduler at the end of the current flow execution, then permit manual
  scheduling by inserting an endpoint URL specifying the flow name into the browser's address bar
  (automated scheduling can be restarted with the *Run* action):

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

