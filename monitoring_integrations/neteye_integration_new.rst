:author: Charles Callaway
:date: 11-10-2022
:modified: 11-10-2022
:tags: integration, monitoring
:lang: en-US
:translation: false
:status: updating

.. include:: ../sphinx-roles.txt



.. _monitoring_integrations_neteye_neps:

#########################
NetEye 4 Integration NEPS
#########################

The procedure below will show you how to integrate your Alyvix test cases into the
:iconlink:`ext|NetEye|https://www.wuerth-phoenix.com/en/solutions/it-system-management/unified-monitoring/`
|trademark| monitoring system.  When the configuration is complete, NetEye will begin to
request the results of Alyvix runs at regular intervals via a NATS channel, and then display
that data in a NetEye Grafana instance with a pre-built template.

The outline of the configuration steps to complete on the NetEye side is:

* Load the **NetEye Extension Packs** which will set up the required infrastructure:
  **Host Templates**, **Service Templates**, etc.
* Customize that infrastructure according to your local requirements, such as inserting the
  names of specific hosts, and a single service check for each Alyvix test case.
* Set up the NATS connection according to the Session Management documentation.
* Check that each host was configured successfully by viewing the incoming Alyvix data
  inside NetEye.


.. _monitoring_integrations_neteye_details_neps:

============================
Detailed Configuration Steps
============================

Although you can carry out the necessary steps by hand, the standardized
:iconlink:`ext|NetEye NEP approach,|https://neteye.guide/current/doc/nep-introduction.html`
and the :iconlink:`ext|Alyvix NEP|https://neteye.guide/current/doc/nep-alyvix/nep-alyvix.html` in
particular, is the only officially supported configuration method.  The following step by step
guide provides the necessary steps in detail.


.. rst-class:: bignums

#. :iconlink:`ext|Follow the Alyvix NEP instructions.|https://neteye.guide/current/doc/nep-alyvix/nep-alyvix.html`
   After ensuring your system meets the basic requirements, the installation process will
   prepare the NetEye infrastructure.

#. Create the certificates.  Pay particular attention here as most problems that do result
   are caused by misnamed or improperly created certificates.  You should decide on a single
   name and use it consistently both in the certificate and in the successive configuration
   steps.

   Certificate creation should result in the following three files:

   * :bolditalic:`Certificate Authority` file with the form :file:`<name>.ca.crt`
   * :bolditalic:`Public Key` file with the form :file:`<name>.crt`
   * :bolditalic:`Private Key` file with the form :file:`<name>.pem.key`, which will be a BASE64
     encrypted text-readable file that should begin with this header:

     .. code-block::

        -----BEGIN PRIVATE KEY-----

   Install them in the appropriate path on the Alyvix Server machine, with restricted permissions
   to ensure the private key cannot be accessed.  You'll need this path in the next step.

#. Follow the :ref:`NATS setup instructions <session_management_nats>`.
   You should use the following default values for a NetEye installation unless told otherwise:

   * **Profile Name:**  ``telegraf_wo``
   * **IP/Port:**  Port ``4222``
   * **Subject Name:**  ``telegraf.metrics``
   * **Measurement Name:**  ``alyvix``

   Also insert the certificate path you used in the previous step.

#. To check that the configuration was successful, select "ITOA" from the NetEye navigation
   bar and choose "Alyvix Troubleshooting View".  Initially the panel will be blank, but
   as the initial results arrive, the data will gradually be displayed.

That's it, you've successfully set up NetEye to visually monitor your Alyvix test cases!

|
