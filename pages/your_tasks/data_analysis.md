---
title: Data analysis
contributors: [Olivier Collin, Stian Soiland-Reyes, Michael R. Crusoe, Sven Twardziok]
description: How to make data analysis FAIR.
page_id: data_analysis
related_pages:
  tool_assembly: [nels, xnat_pic, transmed, ome, galaxy]
training:
  - name: Training in TeSS
    registry: TeSS
    url: https://tess.elixir-europe.org/search?q=%22data+analysis%22#materials
dsw:
- name: How will you make sure to know what exactly has been run?
  uuid: 1991077f-04ae-4808-90a5-e4b2f82e30bf
- name: Did you choose the workflow engine you will be using?
  uuid: a1c37c05-57ff-499c-b58c-e90f511241fa
- name: Will you use a central repository for all tools and their versions as used
    in your project?
  uuid: decb7c9c-c6dc-4027-8c0e-18934c852ca6
- name: How will you work with your data?
  uuid: df36fb68-131c-4f31-a42b-684abf523bbc
faircookbook:
- name: Introducing Provenance Information
  url: https://w3id.org/faircookbook/FCB036
- name: Making Computational Workflows FAIR
  url: https://w3id.org/faircookbook/FCB062
---

## What are the best practices for data analysis?

### Description

When carrying out your analysis, you should also keep in mind that all your data analysis has to be reproducible. This will complement your research data management approach since your data will be FAIR compliant but also your tools and analysis environments. In other words, you should be able to tell what data and what code or tools were used to generate your results.

This will help to tackle reproducibility problems but also will improve the impact of your research through collaborations with scientists who will reproduce your in silico experiments.

### Considerations

There are many ways that will bring reproducibility to your data analysis. You can act at several levels:

* by providing your code;
* by providing your execution environment;
* by providing your workflows;
* by providing your data analysis execution.

### Solutions

* Make your code available. If you have to develop a software for your data analysis, it is always a good idea to publish your code. The git versioning system offers both a way to release your code but offers also a versioning system. You can also use Git to interact with your software users. Be sure to specify a license for your code (see the [licensing section](licensing)).
* Use package and environment management system. By using package and environment management systems like {% tool "conda" %} and its bioinformatics specialized channel {% tool "bioconda" %}, researchers that have got access to your code will be able to easily install specific versions of tools, even older ones, in an isolated environment. They will be able to compile/run your code in an equivalent computational environment, including any dependencies such as the correct version of R or particular libraries and command-line tools your code use. You can also share and preserve your setup by specifying in a [environment file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) which tools you installed.
* Use container environments. As an alternative to package management systems you can consider _container environments_ like {% tool "docker" %} or {% tool "singularity" %}.
* Use workflow management systems. [Scientific Workflow management systems](https://en.wikipedia.org/wiki/Scientific_workflow_system) will help you organize and automate how computational tools are to be executed. Compared to composing tools using a standalone script, workflow systems also help document the different computational analyses applied to your data, and can help with scalability, such as cloud execution. Reproducibility is also enhanced by the use of workflows, as they typically have bindings for specifying software packages or containers for the tools you use from the workflow, allowing others to re-run your workflow without needing to pre-install every piece of software it needs. It is a flourishing field and [many other workflow management systems](https://s.apache.org/existing-workflow-systems) are available, some of which are general-purpose (e.g. any command line tool), while others are domain-specific and have tighter tool integration. Among the many workflow management systems available, one can mention
   * Workflow platforms that manage your data and provide an interface (web, GUI, APIs) to run complex pipelines and review their results. For instance: {% tool "galaxy" %} and {% tool "arvados" %} ({% tool "common-workflow-language" %}-based), open source.
   * Workflow runners that take a workflow written in a proprietary or standardized format (such as the {% tool "common-workflow-language" %}) and execute it locally or on a remote compute infrastructure. For instance, {% tool "cwl-in-toil" %}, the reference CWL runner ({% tool "cwltool" %}), {% tool "nextflow" %}, {% tool "snakemake" %}, {% tool "cromwell" %}.
* Use notebooks. Using notebooks, you will be able to create reproducible documents mixing text and code; which can help explain your analysis choices; but also be used as an exploratory method to examine data in detail. Notebooks can be used in conjunction with the other solutions mentioned above, as typically the notebook can be converted to a script. Some of the most well-known notebooks systems are: {% tool "jupyter" %}, with built-in support for code in Python, R and Julia, and many other {% tool "jupyter-kernels" %}; {% tool "rstudio" %} based on R. See the table below for additional tools.

## How can you use package and environment management systems?

### Description

By using package and environment management systems like {% tool "conda" %} and its bioinformatics specialized channel {% tool "bioconda" %}, you will be able to easily install specific versions of tools, even older ones, in an isolated environment. You can also share and preserve your setup by specifying in a [environment file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) which tools you installed.

### Considerations

Conda works by making a nested folder containing the traditional UNIX directory structure `bin/` `lib/` but installed from Conda's repositories instead of from a Linux distribution.

* As such Conda enables consistent installation of computational tools independent of your distribution or operating system version. Conda is available for Linux, macOS and Windows, giving consistent experience across operating systems (although not all software is available for all OSes).
* Package management systems work particularly well for installing free and Open Source software, but can also be useful for creating an isolated environment for installing commercial software packages; for instance if they requires an older Python version than you have pre-installed.
* Conda is one example of a generic package management, but individual programming languages typically have their environment management and package repositories.
* You may want to consider submitting a release of your own code, or at least the general bits of it, to the package repositories for your programming language.

### Solutions

* MacOS-specific package management systems: {% tool "homebrew" %}, {% tool "macports" %}.
* Windows-specific package management systems: {% tool "chocolatey" %} and {% tool "windows-package-manager" %} `winget`.
* Linux distributions also have their own package management systems (`rpm`/`yum`/`dnf`, `deb`/`apt`) that have a wide variety of tools available, but at the cost of less flexibility in terms of the tool versions, to ensure they exist co-installed.
* Language-specific virtual environments and repositories including: [rvm](https://rvm.io/) and [RubyGems](https://rubygems.org/) for Ruby, [pip](https://docs.python.org/3/installing/index.html) and [venv](https://docs.python.org/3/tutorial/venv.html) for Python, [npm](https://www.npmjs.com/) for NodeJS/Javascript, [renv](https://rstudio.github.io/renv/) and [CRAN](https://cran.r-project.org/) for R, [Apache Maven](https://maven.apache.org/) or [Gradle](https://gradle.org/) for Java.
* Tips and tricks to navigate the landscape of software package management solutions:
    * Manage the software you need in an OS-independent way by listing all relevant packages in your Conda environment via the `environment.yaml` file.
    * If you need conflicting versions of some tools/libraries for different operations, make separate Conda environments.
    * If you need a few open source libraries for your Python script, none of which require compiling, make a `requirements.txt` and reference `pip` packages.

## How can you use container environments?

### Description

Container environments like {% tool "docker" %} or {% tool "singularity" %} allow you to easily install specific versions of tools, even older ones, in an isolated environment.

### Considerations

In short containers works almost like a virtual machine (VMs), in that it re-creates a whole Linux distribution with separation of processes, files and network.
* Containers are more lightweight than VMs since they don't virtualize hardware. This allows a container to run with a fixed version of the distribution independent of the host, and have just the right, minimal dependencies installed.
* The container isolation also adds a level of _isolation_, which although not as secure as VMs, can reduce the attack vectors. For instance if the database container was compromised by unwelcome visitors, they would not have access to modify the web server configuration, and the container would not be able to expose additional services to the Internet.
* A big advantage of containers is that there are large registries of community-provided container images.
* Note that modifying things inside a container is harder than in a usual machine, as changes from the image are lost when a container is recreated.
* Typically containers run just one tool or applications, and for service deployment this is useful for instance to run mySQL database in a separate container from a NodeJS application.

### Solutions

* {% tool "docker" %} is the most well-known container runtime, followed by {% tool "singularity" %}. These require (and could be used to access) system administrator privileges to be set up.
* {% tool "udocker" %} and {% tool "podman" %} are also _user space_ alternatives that have compatible command line usage.
* Large registries of community-provided container images are {% tool "podman" %} and [RedHat Quay.io](https://quay.io/search). These are often ready-to-go, not requiring any additional configuration or installations, allowing your application to quickly have access to open source server solutions.
* {% tool "biocontainers" %} have a large selection of bioinformatics tools.
* To customize a Docker image, it is possible to use techniques such as {% tool "volumes" %} to store data and {% tool "dockerfile-reference" %}. This is useful for installing your own application inside a new container image, based on a suitable _base image_ where you can do your `apt install` and software setup in a reproducible fashion - and share your own application as an image on {% tool "docker-hub" %}.
* Container linkage can be done by _container composition_ using tools like {% tool "docker-compose-overview" %}.
* More advanced container deployment solutions like {% tool "kubernetes" %} and Computational Workflow Management systems can also manage cloud instances and handle analytical usage.
* {% tool "openstack" %} is an open-source platform that uses pooled virtual resources to build and manage private and public clouds. It provides a stable base for deploying and managing containers, allowing for faster application deployment and simplified management.
* Tips and tricks to navigate the landscape of container solutions:
    * If you just need to run a database server, describe how to run it as a Docker/Singularity container.
    * If you need several servers running, connected together, set up containers in Docker Compose.
    * If you need to install many things, some of which are not available as packages, make a new `Dockerfile` recipe to build container image.
    * If you need to use multiple tools in a pipeline, find Conda or container images, compose them in a Computational Workflow.
    * If you need to run tools in a cloud instance, but it has nothing preinstalled, use Conda or containers to ensure installation on cloud VM matches your local machine.
    * If you just need a particular open source tool installed, e.g. ImageMagick, check the document how to install: _For Ubuntu 20.04, try `apt install imagemagick`_.
* Domain specific solutions that make use of containers to benchmark and reproducibly deploy workflows exist, including {% tool "biaflows" %} for bioimage data.

## How can you use workflow management systems for reproducible data analysis?

### Description

Using containerization together with workflow management systems provides several benefits for data analysis, including:

* Reproducibility: By using containerized environments and workflow management systems, you can ensure that your analysis is reproducible, as the environment in which the analysis is executed is exactly the same each time.
* Portability: Containerized environments can be easily moved between different computing environments, allowing you to execute your analysis on different computing resources or share your analysis with collaborators.
* Scalability: Workflow management systems can be used to execute analyses on large computing clusters (like the EuroHPC supercomputer {% tool "lumi" %}) or cloud computing resources, enabling you to scale your analysis as needed.

### Considerations

Creating an analysis workflow involves several steps that require careful consideration. The following steps can help you create a workflow and run it locally or in the cloud:

* Before creating a workflow, it is important to define the scope and objectives of the analysis. This will help you to determine the type of data to collect, the analysis methods to use, and the resources required for the analysis.
* After defining the scope and objectives, the next step is to determine the tools and software to use. You need to choose software that is compatible with the type of data you want to analyze and the analysis methods you plan to use.
* Once you have determined the tools and software to use, the next step is to create the workflow. This involves breaking down the analysis process into small, manageable steps that can be automated. Each step should be clearly defined, and the inputs and outputs of each step should be documented.
* If you want to use containers, you can now define the container images for the execution of the entire workflow or for the individual steps.
* After creating the workflow, it is important to test it to ensure that it works as expected. You can do this by running a test dataset through the workflow and checking the outputs to ensure they match the expected results.
* Once you have tested the workflow, the next step is to run it on your dataset. Depending on the size of your data, you can run the workflow locally on your computer or on a remote workflow management system.

### Solutions

- Most workflow management systems provide detailed tutorials and documentation for creating workflows and including containerization technologies. Here are documentations for [Nextflow](https://nextflow.io/docs/latest/container.html#docker), [Snakemake](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html), [Cromwell](https://cromwell.readthedocs.io/en/stable/tutorials/Containers/), [CWL](https://www.commonwl.org/user_guide/topics/using-containers.html).
- The {% tool "biocontainers" %} project provides a platform for storing and sharing containers that can used in your workflow.
- The {% tool "bio-tools" %} repository lists state of the art tools and databases from the field of bioinformatics ordered by collections and communities.
- {% tool "openebench" %} is a framework for monitoring and  benchmarking analysis tools and workflows.
- {% tool "workflowhub" %} and {% tool "dockstore" %} are two popular services for sharing and re-using workflows.
- {% tool "life-monitor" %} is a service designed to facilitate the long-term viability and reusability of published computational workflows.
- The [ELIXIR Cloud and AAI project](https://elixir-cloud-aai.github.io/) supports a framework for executing workflows in the cloud via the standards developed by the [GA4GH](https://www.ga4gh.org/) community.

