## Azure Virtual Machines

- **Azure Virtual Machines (VMs)** are scalable, on-demand computing resources provided by Microsoft Azure.
- VMs allow you to run Windows or Linux operating systems in the cloud, similar to running them on physical hardware.
- You can choose VM size, storage, and networking options to match your workload requirements.
- VMs can be used for development, testing, hosting applications, or extending your on-premises datacenter.
- Azure provides features like automated scaling, load balancing, and integrated security for VMs.
- You are responsible for managing the operating system, applications, and data on your VMs, while Azure manages the underlying infrastructure.

## 99.99% Availability

- **99.99% availability** means that a service is guaranteed to be operational 99.99% of the time within a given period (usually a month).
- This equates to less than 5 minutes of downtime per month.
- Azure achieves high availability through features like regions, availability zones, redundant infrastructure, and automated failover.
- Service Level Agreements (SLAs) define the guaranteed uptime for Azure services; many core services offer a 99.99% SLA when deployed across multiple availability zones.
- High availability is critical for mission-critical applications that require minimal downtime and continuous access.

## Availability Sets

- **Availability Sets** are a feature in Azure that help ensure high availability for virtual machines (VMs) by distributing them across multiple isolated hardware resources within a datacenter.
- An availability set consists of two key concepts:
    - **Update domains (UDs):** Group VMs so that they are rebooted together during planned maintenance. Azure never reboots all UDs at once.
    - **Fault domains (FDs):** Group VMs so that they share a common power source and network switch. VMs in different FDs are isolated from each other to reduce the risk of simultaneous hardware failures.
- By placing VMs in an availability set, you protect your application from single points of failure due to hardware or maintenance events.
- Availability sets are recommended for workloads that require high uptime, such as application servers and database servers.
- Azure provides a 99.95% SLA for VMs deployed in an availability set.

> **Tip:**  
Always deploy at least two VMs in an availability set to maximize fault tolerance and meet Azure's high availability guarantees.

## Virtual Machine Scale Sets

- **Virtual Machine Scale Sets (VMSS)** are Azure compute resources that allow you to deploy and manage a group of identical, load-balanced VMs.
- VMSS automatically increase or decrease the number of VM instances in response to demand or a defined schedule.
- All VMs in a scale set are configured the same, making it easy to manage and update applications at scale.
- VMSS integrates with Azure Load Balancer and Application Gateway for high availability and traffic distribution.
- Common use cases include large-scale applications, microservices, and workloads that require elastic scaling.
- VMSS supports both Windows and Linux VMs and can be managed using the Azure portal, CLI, or ARM templates.

## Azure Functions

- **Azure Functions** is a serverless compute service that enables you to run event-driven code without managing infrastructure.
- Functions are triggered by events such as HTTP requests, timers, or messages from other Azure services.
- You only pay for the compute resources your code consumes while it runs.
- Supports multiple programming languages, including C#, JavaScript, Python, and PowerShell.
- Ideal for automating tasks, integrating systems, processing data, and building APIs.
- Azure automatically handles scaling, availability, and patching for your functions.
- Functions can be developed, tested, and deployed using the Azure portal, CLI, or integrated development environments.

## Meaning of Serverless

- **Serverless computing** is a cloud computing model where the cloud provider automatically manages the infrastructure required to run your code.
- Developers focus on writing code, while Azure handles provisioning, scaling, and maintaining servers.
- You are billed only for the compute resources your code actually uses, rather than for pre-allocated server capacity.
- Serverless services in Azure include Azure Functions and Azure Logic Apps.
- Serverless is ideal for event-driven workloads, microservices, and applications with unpredictable or variable usage patterns.
- Benefits include reduced operational overhead, automatic scaling, and faster time to market.

## Azure App Service

- **Azure App Service** is a fully managed platform for building, deploying, and scaling web apps, RESTful APIs, and mobile backends.
- Supports multiple programming languages, including .NET, Java, Node.js, Python, and PHP.
- Provides built-in features such as custom domains, SSL certificates, authentication, and continuous deployment from popular source control systems.
- Automatically handles infrastructure maintenance, patching, and scaling.
- Enables easy integration with other Azure services and DevOps workflows.
- Offers different pricing tiers to match development, testing, and production needs.
- Ideal for hosting web applications with high availability and security requirements.

## Microservices

- **Microservices** is an architectural approach where an application is structured as a collection of small, independent services that communicate over APIs.
- Each microservice is responsible for a specific business capability and can be developed, deployed, and scaled independently.
- Microservices enable teams to use different technologies and programming languages for each service, improving flexibility and innovation.
- This architecture supports faster development cycles, easier maintenance, and greater resilience, as failures in one service do not impact the entire application.
- Azure provides tools and services such as Azure Kubernetes Service (AKS), Azure Service Fabric, and Azure Functions to build, deploy, and manage microservice-based applications.
- Microservices are ideal for complex, large-scale applications that require agility, scalability, and continuous delivery.

## Azure Container Instances

- **Azure Container Instances (ACI)** provide a fast and easy way to run containers in Azure without managing virtual machines or orchestrators.
- You can deploy containers using images from public or private registries, such as Docker Hub or Azure Container Registry.
- ACI supports both Linux and Windows containers, and allows you to specify CPU, memory, and networking resources.
- Containers start in seconds and are billed per second for the resources consumed.
- Ideal for scenarios like simple application hosting, batch jobs, data processing, and development/testing environments.
- ACI integrates with other Azure services and can be used as part of larger solutions, such as with Azure Logic Apps or Azure Kubernetes Service (AKS) for burst workloads.
- Provides isolation, secure networking, and the ability to define environment variables and persistent storage for containers.


## Azure Kubernetes Service (AKS)

- **Azure Kubernetes Service (AKS)** is a managed Kubernetes container orchestration service provided by Azure.
- AKS simplifies deploying, managing, and scaling containerized applications using Kubernetes.
- Azure handles critical tasks such as cluster provisioning, upgrades, patching, and scaling, reducing operational overhead.
- AKS integrates with Azure Active Directory, monitoring, and networking services for enhanced security and management.
- Supports both Linux and Windows containers, and enables automated scaling and self-healing of applications.
- Ideal for running microservices, distributed systems, and applications that require high availability and scalability.
- Developers can use familiar Kubernetes tools (kubectl, Helm) and CI/CD pipelines to deploy and manage workloads on AKS.


## Azure Service Fabric

- **Azure Service Fabric** is a distributed systems platform for building and managing scalable, reliable microservices and container-based applications.
- Supports both stateless and stateful microservices, making it suitable for complex, data-intensive workloads.
- Provides built-in capabilities for service discovery, health monitoring, automatic scaling, rolling upgrades, and self-healing.
- Enables deployment on Azure, on-premises, or other clouds, supporting hybrid and multi-cloud scenarios.
- Service Fabric powers core Azure services, demonstrating its reliability and scalability.
- Developers can use .NET, Java, or any language with container support to build applications on Service Fabric.
- Ideal for mission-critical applications that require low latency, high throughput, and continuous availability.
