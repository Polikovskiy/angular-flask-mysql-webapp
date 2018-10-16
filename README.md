Overview
Imagine you are a VPN gateway administrator. You store data about your companies (company name and monthly transfer quota), users (company, email) and all transfers (url, when it occurred and amount of bytes transferred).
You need an interface to manage your users and companies and view a report.
Last week you’ve been at the frontend development conference and heard that JSON REST API is the industry standard nowadays and you decided to create your own tool for your task using this approach.

Requirements

There are four screens in the application: user management, company management, view all companies that exceed quota and view users from all the blocked companies that transferred more than others from the same company (abusers).
Application interface consists of 3 tabs or pages: Companies, Users, Abusers. It would be nice to see a single-page application here, but it’s not a requirement.
Note, that also we’ve got some ideas on the look & feel of the application and components you could use (see below), we are flexible about the frontend implementation. You will not be judged based on the appearance of the interface.
