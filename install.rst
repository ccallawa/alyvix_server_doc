:author: Charles Callaway
:date: 05-11-2020
:modified: 24-11-2020
:tags: install, python, pip
:lang: en-US
:translation: false
:status: final

.. include:: sphinx-roles.txt


.. _install_top:

************************
Installation and Upgrade
************************

Before installing Alyvix, first check that your setup meets the system requirements.

|


.. _system_requirements_top:

===================
System Requirements
===================

.. note::

   Alyvix assumes that you have one virtual or physical machine exclusively dedicated to running
   Alyvix test cases.

You should check that your designated machine and the account on that machine meet the following
requirements before you install Alyvix:

+---------------------+--------------------------------+-----------------------------------------+
|                     | Minimum                        | Recommended                             |
+---------------------+--------------------------------+-----------------------------------------+
| :file:`Operating`   | **Windows 10 (64-bit)**        | **Windows Server 2016, 2019 or 2022**   |
| :file:`System`      | **Pro or Enterprise**          | (English language)                      |
|                     +--------------------------------+-----------------------------------------+
|                     | (32-bit versions of Windows are :warn:`not` compatible with Alyvix)      |
+---------------------+--------------------------------+-----------------------------------------+
| :file:`Processor`   | 2 CPUs                         | 2 CPUs base **+** 2 CPUs per session    |
+---------------------+--------------------------------+-----------------------------------------+
| :file:`Memory`      | 4GB RAM                        | 4GB RAM base **+** 4GB RAM per session  |
+---------------------+--------------------------------+-----------------------------------------+
| :file:`Graphics`    | 24-bit RGB or 32-bit RGBA screen color depth                             |
+---------------------+--------------------------------+-----------------------------------------+
| :file:`Remote`      | Users defined on Alyvix Server must have RDP access (through RDC         |
| :file:`Desktop`     | *mstsc.exe*) to the machine itself (e.g. the user must be a Remote       |
|                     | Desktop User, and the firewall must not be set to block local RDC)       |
|                     +--------------------------------+-----------------------------------------+
|                     | **1 session only:** No Windows | **Multiple sessions in parallel:**      |
|                     | Terminal Server available;     | Windows Terminal Server allows          |
|                     | 1 test case executed at a time | multiple test cases to run at once      |
+---------------------+--------------------------------+-----------------------------------------+
| :file:`Application` | Users defined on Alyvix Server must have the proper permissions          |
| :file:`Permissions` | to run and interact with the application interface being monitored       |
+---------------------+--------------------------------+-----------------------------------------+
| :file:`Networks`    | Alyvix Server must be reachable from an external browser                 |
+---------------------+--------------------------------+-----------------------------------------+

|


.. _installation_versions:

========
Versions
========

+-----------------------------------+----------------------------------+---------------------------------+
| Alyvix Server Version             | Required Alyvix Version          | PostgreSQL Version              |
+-----------------------------------+----------------------------------+---------------------------------+
| Alyvix Server 1.7.3               | |link-to-alyvix-install331|      | |link-postgresql-install-12.x|  |
+-----------------------------------+----------------------------------+---------------------------------+
| Alyvix Server 1.6.0               | |link-to-alyvix-install323|      | |link-postgresql-install-12.x|  |
+-----------------------------------+----------------------------------+---------------------------------+
| Alyvix Server 1.5.0               | |link-to-alyvix-install320|      | |link-postgresql-install-12.x|  |
+-----------------------------------+----------------------------------+---------------------------------+

|


.. _installation_steps:

==================
Installation Steps
==================

The following steps will install Alyvix Server on your machine:

.. rst-class:: bignums

#. Install Python

   Follow `the same instructions <https://www.alyvix.com/learn/getting_started/install.html#installing-python>`_
   as for Alyvix

#. Install Alyvix

   Follow the `Alyvix installation instructions <https://www.alyvix.com/learn/getting_started/install.html#installing-alyvix>`_

#. Install PostgreSQL 12.x

   Download and run
   `the PostgreSQL installer <https://content-www.enterprisedb.com/postgresql-tutorial-resources-training?cid=48>`_

#. Install Alyvix Server

   * `Get the software package <https://www.alyvix.com/service#plans>`_
   * Run the :file:`setup.exe` installer
   * Set the database password as follows:

      * Open the file :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\config.json`
      * Set your own password in this line: |br|
        ``"database":{.. "password": "<your_password>", ..}``

#. Install your HTTPS certificate

   Save your files as follows:

   * Go to the folder :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\cert\\`
   * Save :file:`cert.crt` as an HTTPS certificate recognized by your CA
   * Save :file:`cert.key` as its (unprotected) password

   Note that the private key is all you need, you should not be asked for an additional password.

#. Run **Alyvix Service** within Windows Services

|


.. _install_upgrade:

=========
Upgrading
=========

The following steps will upgrade Alyvix Server to the latest version on your machine:

.. rst-class:: bignums

#. Uninstall Alyvix Server

   * Back up your Alyvix Server configuration file:  :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\config.json`
   * Back up your Alyvix Server HTTPS certificate:  :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\cert\\`
   * Stop Alyvix Server:  **Windows Services > Alyvix Service > Stop**
   * Close all Alyvix client windows (where appropriate)
   * Uninstall Alyvix Server:  **Windows Control Panel > Programs and Features > Alyvix Server > Uninstall**
   * Remove residual Alyvix Server files (where appropriate):  :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\`
   * Remove old Alyvix Client scheduled tasks:  **Windows Task Scheduler > alyvix_client<..> > delete**

#. Upgrade Alyvix

   Follow `the instructions here <https://alyvix.com/learn/getting_started/install.html#upgrading-alyvix>`_

#. Install the new Alyvix Server

   * Run the Alyvix Server Installer (:file:`setup.exe`) found in the Alyvix Server package
   * Set a database password (or restore the backup file):
     :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\config.json` **> "password": "<your_password>"**
   * Install your HTTPS certificate (or restore the backup files):  Save the :file:`cert.crt` and
     :file:`cert.key` files in :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\cert\\`

#. Run Alyvix Server

   * Start the Alyvix Service:  **Windows Services > Alyvix Service > start**
   * Sign out of the current session

|
