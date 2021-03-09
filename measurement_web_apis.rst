:author: Charles Callaway
:date: 22-09-2020
:modified: 02-11-2020
:tags: index
:lang: en-US
:translation: false
:status: final

.. include:: sphinx-roles.txt



.. _measurement_web_apis_top:

====================
Measurement Web APIs
====================

The measurements API provides read-only access to both configurations and recorded data, such as
the results of test case runs.  There are two principal ways to retrieve measurement data:

* Directly as data in JSON format (see below) from the measurement database with a RESTful Web
  API request
* As a :ref:`human readable report <transaction_reporting_top>` in HTML format from a transaction
  reporting  RESTful Web API request

.. warning::

   All API level 0 endpoints (marked "/v0/" in Alyvix Server v1.4.2) are insecure.  They should
   only be used when both caller and server are contained entirely within the same private
   network.



.. _measurement_web_apis_endpoints:

*************************
Measurement API Endpoints
*************************

The following table lists the available measurement endpoints, along with their return values,
whether as measurement data encoded in JSON objects, or as viewable reports in HTML.

If you frequently need to view the JSON structures that Alyvix Server produces, we recommend the
use of the free **JSON Viewer Pro**
`Chrome browser extension <https://chrome.google.com/webstore/search/json%20viewer%20pro>`_.

.. table::
   :class: endpoint-table

   +---------+--------------------------------------------------------------------------------------------------+
   | Returns | Measurement Web API Endpoints (v0)                                                               |
   +---------+--------------------------------------------------------------------------------------------------+
   | JSON    | :ep-head:`<alyvix_server>/v0/testcases`                                                          |
   |         |                                                                                                  |
   |         | |tab| Returns a JSON list containing the                                                         |
   |         | :ref:`settings for registered testcases <session_management_test_cases>`: **name**,              |
   |         | **arguments**, **alias**, **screenshot recording** and **screenshot compression**, where each    |
   |         | registered test case is :ref:`a separate entry <measurement_web_apis_testcase_example>` in the   |
   |         | list                                                                                             |
   +---------+--------------------------------------------------------------------------------------------------+
   | JSON    | :ep-head:`<alyvix_server>/v0/testcases/<testcasealias>`                                          |
   |         |                                                                                                  |
   |         | |tab| Returns the most recent *measures* substructures                                           |
   |         | (:ref:`full example below <measurement_web_apis_measures_example>`) from the session where the   |
   |         | test case alias is enabled, along with the *repolling_period*, which is automatically calculated |
   |         | whenever you change the scheduling period as |smalltab| :bolditalic:`SchedulingPeriod / 2`.      |
   +---------+--------------------------------------------------------------------------------------------------+
   | JSON    | :ep-head:`<alyvix_server>/v0/testcases/<testcasealias>?screenshots=[true, false]`                |
   |         |                                                                                                  |
   |         | |tab| This returns the same structure as the *<testcasealias>* endpoint, but if the parameter is |
   |         | set to *true*, then Base64 screenshots (including annotations) will be included in the JSON      |
   |         | (default = *false*)                                                                              |
   +---------+--------------------------------------------------------------------------------------------------+
   | HTML    | :ep-head:`<alyvix_server>/v0/testcases/<testcasealias>/reports`                                  |
   |         |                                                                                                  |
   |         | |tab| Produces a human-readable report (list) in reverse chronological order, showing the        |
   |         | following information for each run:  **Timestamp**, **Runcode**, **Hostname**, and **Username**  |
   +---------+--------------------------------------------------------------------------------------------------+
   | HTML    | :ep-head:`<alyvix_server>/v0/testcases/<testcasealias>/reports?runcode=<runcode>`                |
   |         |                                                                                                  |
   |         | |tab| Displays the human-readable details of a single (successful or failed) test case           |
   +---------+--------------------------------------------------------------------------------------------------+
   | JSON    | :ep-head:`<alyvix_server>/v0/flows/run?username=<domain\\username>`                              |
   |         |                                                                                                  |
   |         | |tab| If a session has been                                                                      |
   |         | :ref:`set as manual in the scheduler <test_case_flow_management_actions>`, then you can  run a   |
   |         | specific, defined workflow a single time by calling this endpoint URL                            |
   +---------+--------------------------------------------------------------------------------------------------+


.. _measurement_web_apis_testcase_example:

.. topic::  Testcases

   An example *testcases* JSON structure:

.. code-block:: json
   :linenos:

   {
      "testcases": [
         {
            "testcase_name": "test",
            "testcase_arguments": "me",
            "testcase_alias": "test_me",
            "screenshot_recording": "any-output",
            "screenshot_compression": "compressed"
         },
      ]
   }


.. _measurement_web_apis_measures_example:

.. topic:: **Measures** JSON structure

   The detailed *measures* JSON structure:

.. code-block:: json
   :linenos:

   {
      "measures": [
         {
            "timestamp_epoch": 1601281337776667400,
            "hostname": "pbzalyvixts01",
            "domain_username": "WP\\AlyvixUser01",
            "test_case_name": "visittrentino",
            "test_case_arguments": null,
            "test_case_alias": "visittrentino",
            "test_case_execution_code": "pb01Al01vino1601281335",
            "test_case_duration_ms": 52904,
            "test_case_exit": "true",
            "test_case_state": 0,
            "transaction_name": "vt_home_ready",
            "transaction_alias": "vt_home_ready",
            "transaction_group": null,
            "transaction_detection_type": "appear",
            "transaction_timeout_ms": 10000,
            "transaction_warning_ms": null,
            "transaction_critical_ms": null,
            "transaction_performance_ms": 2005,
            "transaction_accuracy_ms": 116,
            "transaction_exit": "true",
            "transaction_state": 0,
            "transaction_record_text": "",
            "transaction_record_extract": "",
            "transaction_resolution_width": 1280,
            "transaction_resolution_height": 800,
            "transaction_scaling_factor": 100
         }
      ],
      "repolling_period": 5
   }

|
