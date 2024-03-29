:author: Charles Callaway
:date: 04-05-2021
:modified: 04-05-2021
:tags: integration, monitoring
:lang: en-US
:translation: false
:status: updating

.. include:: sphinx-roles.txt



.. _monitoring_integrations_top:

##############################
Monitoring System Integrations
##############################

The procedure linked to below will show you how to configure various monitoring system
installations to request the results of Alyvix runs at regular intervals, thus integrating
Alyvix test cases into your monitoring system.  Over time the data collected can indicate
trends that can help you discover when the user experience is below expectations and
locate hardware bottlenecks.

The monitoring systems below have been tested for compatibility with Alyvix.  To see the
configuration tutorial for a particular system, click on the monitoring system link in the
first column, or in the index at the left.  Integration tutorials for additional monitoring
systems will be added as they become available.

|


.. logos should be around 58x53 and png

.. |ne-logo| image:: monitoring_integrations/images/neteye-logo.png
   :scale: 40%

.. |chk-logo| image:: monitoring_integrations/images/chkmk-logo.png
   :scale: 40%

.. |prtg-logo| image:: monitoring_integrations/images/prtg-logo.png
   :scale: 40%

.. table::
   :class: taller-rows all-white-rows
   :widths: 70 30

   +--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
   | Monitoring System Integration Instructions                                                                               | Developer                                                                                                                 |
   +--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
   | |smalltab| |chk-logo| |trade| |smalltab| :ref:`Checkmk  2 instructions <monitoring_integrations_checkmk>`                | :iconlink:`ext|tribe29|https://checkmk.com/`                                                                              |
   +--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
   | |smalltab| |ne-logo| |trade| |smalltab| :ref:`NetEye 4 instructions <monitoring_integrations_neteye>`                    | :iconlink:`ext|Wuerth Phoenix|https://www.wuerth-phoenix.com/en/solutions/it-system-management/unified-monitoring/` |tab| |
   +--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
   | |smalltab| |ne-logo| |trade| |smalltab| :ref:`NetEye 4 instructions NEPS <monitoring_integrations_neteye_neps>`          | :iconlink:`ext|Wuerth Phoenix|https://www.wuerth-phoenix.com/en/solutions/it-system-management/unified-monitoring/` |tab| |
   +--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
   | |smalltab| |prtg-logo| |trade| |smalltab| :ref:`PRTG Network Monitor 21 instructions <monitoring_integrations_prtg>`     | :iconlink:`ext|Paessler|https://www.paessler.com/prtg/`                                                                   |
   +--------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

|



.. toctree::
   :maxdepth: 2
   :name: toc_monitoring_integrations
   :hidden:

   monitoring_integrations/checkmk_integration.rst
   monitoring_integrations/neteye_integration.rst
   monitoring_integrations/neteye_integration_new.rst
   PRTG Network Monitor 21 <monitoring_integrations/prtg_integration.rst>
