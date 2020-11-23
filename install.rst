:author: Charles Callaway
:date: 05-11-2020
:modified: 23-11-2020
:tags: install, python, pip
:lang: en-US
:translation: false
:status: final

.. include:: sphinx-roles.txt


.. _install_top:

============
Installation
============

Before installing Alyvix, first check that your setup meets the system requirements.

|



.. _system_requirements_top:

.. topic::   System Requirements

   .. note::

      Alyvix assumes that you have one virtual or physical machine exclusively dedicated to running
      Alyvix test cases.

You should check that your designated machine meets the following requirements before you install
Alyvix:

.. admonition::  Requirements
   :class: warning

   * Screen color depth: 24-bit RGB or 32-bit RGBA
   * OS: **Windows 64-bit** 10, Server 2012, 2016 or 2019
     (32-bit versions of Windows are :warn:`not` compatible with Alyvix)



.. _installation_steps:

.. topic::   Installation Steps

   The following steps will install Alyvix Server on your machine:

.. rst-class:: bignums

#. Install Python

   Follow `the same instructions <https://www.alyvix.com/learn/getting_started/install.html#installing-python>`_
   as for Alyvix

#. Install Alyvix

   Follow `the same instructions <https://www.alyvix.com/learn/getting_started/install.html#installing-alyvix>`_
   as for Alyvix

#. Install PostgreSQL 12.4

   Download and run
   `the PostgreSQL installer <https://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=48>`_

#. Install Alyvix Server

   * `Get the software package <https://www.alyvix.com/service#plans>`_
   * Run the :file:`setup.exe` installer
   * Set the database password as follows:

      * Open the file :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\config.json`
      * Set your own password in this line: ``"database":{.. "password": "<your_password>", ..}``

#. Install your HTTPS certificate

   Save your files as follows:

   * Go to the folder :file:`C:\\Program Files\\Alyvix\\Alyvix Server\\cert\\`
   * Save :file:`cert.crt` as an HTTPS certificate recognized by your CA
   * Save :file:`cert.key` as its (unprotected) password

#. Run **Alyvix Service** within Windows Services

|



.. _install_upgrade:

*********
Upgrading
*********

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
