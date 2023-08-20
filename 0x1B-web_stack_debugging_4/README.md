# 0x1B. Web stack debugging #4

### Web Stack Debugging and OS Configuration Documentation

Requirements:

-    Ubuntu 14.04 LTS
-    Puppet v3.4
-    Puppet manifests must pass puppet-lint version 2.1.1 without errors
=    Puppet manifests must run without error
-    Files should end with a new line
-    README.md file at the root of the project folder is mandatory


### Task 0: Web Stack Debugging

**Objective**: Optimize Nginx configuration to handle high traffic loads and reduce failed requests.

**Problem**: A web server setup with Nginx is experiencing a large number of failed requests.

**Solution**:
This task addresses Nginx optimization by configuring key settings to handle high traffic:

-    Adjust worker connections to 4000 for better throughput.
-    Enable various performance-enhancing options.
-    Add custom header "X-Served-By" for identification.
-    Ensure Nginx is installed and running.


### Task 1: OS Configuration

Objective: Allow the holberton user to login and open files without encountering error messages related to file limits.

Problem: The holberton user is unable to log in and open files without encountering "Too many open files" errors.

Solution:

This task configures system limits for the holberton user to prevent "Too many open files" errors:

-    Create the holberton user, ensuring home directory management and shell.
-    Define ulimit configuration for the holberton user.
-    Configure PAM limits for the holberton user.
-    Implement the reload of PAM configuration.

These solutions enhance user experience by addressing user access and file limit issues on the system.

**Documentation Summary**:
This brief documentation explains two tasks' objectives, problems, and their solutions using Puppet manifests. It provides concise summaries of how each manifest addresses the challenges faced and offers solutions to improve system performance and user experience. The documentation meets project requirements and succinctly captures the essence of the tasks and solutions.
