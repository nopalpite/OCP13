Deployment
==========

Prerequisites
~~~~~~~~~~~~~

- GitHub account
- CircleCI account (linked to GitHub account)
- Docker account
- Render account
- Sentry account

CircleCI
~~~~~~~~

1. Go to CircleCI (https://circleci.com) and sign in with your GitHub account.

2. Click "Add Projects" to add your OCP13 project to CircleCI.

3. Select the project from the list and click "Set Up Project."

4. CircleCI will automatically detect your .circleci/config.yml file in your GitHub repository and start running builds whenever you make code changes.

5. Go to your project settings and set up your environment variable:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Variable Name
     - Description
   * - DOCKER_LOGIN
     - Docker Hub username/login
   * - DOCKER_PASSWORD
     - Docker Hub password or access token
   * - DOCKER_REPO
     - Docker repository name
   * - RENDER_HOOK
     - Render webhook secret
   * - SECRET_DJANGO_KEY
     - Django secret key for your application
   * - SENTRY_DSN
     - Sentry DSN for error tracking

Docker
~~~~~~

Create a DockerHub repository. The repository name must match the DOCKER_REPO variable set in CircleCI.

The CircleCI workflow will build and push the app image in the DockerHub repository.
All images are tagged with the CircleCI commit “hash” ($CIRCLE_SHA1).

Sentry
~~~~~~

After creating a Sentry account, set up a Django project.
You'll receive a unique DSN (Data Source Name) during this process, which you'll need to configure Sentry within your project.

Use this DSN to configure your environment variable within Django and CircleCI.

Render
~~~~~~

1. Create a Render account with GitHub.

2. Click "New" and then "Web Service."

3. Select your public GitHub repository.

4. Configure your project by naming it and selecting "Docker" in the "Runtime" option. In the advanced options, add the following environment variables and select "No" in the "Auto-Deploy" option:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Variable Name
     - Description
   * - SECRET_KEY
     - Your Django project's SECRET_KEY
   * - SENTRY_DSN
     - Your Sentry project's DSN key

5. Use the Deploy Hook in CircleCi environment variable