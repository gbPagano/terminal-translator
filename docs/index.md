# Getting Started

Terminal Translator is a translation CLI that uses the [Google Cloud API](https://cloud.google.com/translate).

## Installation

Installation is very simple, just run the following command in the terminal:

```bash
pip install terminal-translator
```

!!! tip "We recommend trying [pipx](https://github.com/pypa/pipx)"
    pipx is a tool to help you install and run end-user applications written in Python.

    ```pipx install terminal-translator```




## Configuration

To start using the CLI, first we need to configure the access credentials for the goole API.

Login to the [Google Cloud API](https://cloud.google.com/translate), and click start free.

![Step 1](assets/images/config-01.png)

!!! notes "A credit card will be required but don't worry, there will be no charge."

Go to the google cloud console home page and create a new project

![Step 2](assets/images/config-02.png)

![Step 3](assets/images/config-03.png)

Give the project any name

![Step 4](assets/images/config-04.png)

Select the project, and save the project-id

![Step 5](assets/images/config-05.png)

Search for Cloud Translation API and enable it

![Step 6](assets/images/config-06.png)

Create an access credential
!!! warning "Be aware of the usage quota limit"
    Don't share your credentials

![Step 7](assets/images/config-07.png)

![Step 8](assets/images/config-08.png)

Give the service account any name

![Step 9](assets/images/config-09.png)

Go back to the API page and select your service account, and create a new Json type key

A json file containing your credentials will be downloaded

![Step 10](assets/images/config-10.png)

![Step 11](assets/images/config-11.png)

Go back to your service accounts and copy the respective email

![Step 12](assets/images/config-12.png)

In the IAM session, grant access to this email and assing the role Cloud Translation API Admin

![Step 13](assets/images/config-13.png)

![Step 14](assets/images/config-14.png)

Now with the configured service credentials we can go to the CLI


Use the `tt-configure` command passing two arguments, first the project-id followed by the path of the credentials Json file.

```bash
tt-configure <project-id> <google-api-credentials>
```

![Step 15](assets/images/tt-configure-2.png)

Finished! Now you are ready to use the Terminal Translator CLI

See the [tutorial session](/tutorial) to learn about the basic usage
