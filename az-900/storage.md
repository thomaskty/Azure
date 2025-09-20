
# Azure Storage Types and Tiers
## Storage Types
- **Blob Storage**: Object storage for unstructured data such as documents, images, videos, and backups.
- **File Storage (Azure Files)**: Managed file shares accessible via SMB and NFS protocols.
- **Queue Storage**: Messaging store for reliable messaging between application components.
- **Table Storage**: NoSQL key-value store for structured, non-relational data.
- **Disk Storage**: Persistent, high-performance block storage for Azure Virtual Machines.

## Storage Tiers
- **Hot Tier**: Optimized for storing data that is accessed frequently. Higher storage costs, lower access costs.
- **Cool Tier**: For infrequently accessed data that needs to be stored for at least 30 days. Lower storage costs, higher access costs than Hot.
- **Archive Tier**: For rarely accessed data that can tolerate several hours of retrieval latency. Lowest storage cost, highest access cost.

# Azure Storage Explorer and Storage Browser
## Azure Storage Explorer
- **Azure Storage Explorer** is a free, standalone desktop application from Microsoft for managing Azure storage resources.
- Allows you to easily view, upload, download, and organize data in Azure Blob Storage, Azure Files, Queues, and Tables.
- Supports managing storage accounts across multiple Azure subscriptions and tenants.
- Enables access to storage resources using Azure AD, shared access signatures (SAS), or account keys.
- Useful for troubleshooting, data migration, and day-to-day management tasks.

## Storage Browser (Azure Portal)
- The **Storage browser** is a web-based tool integrated into the Azure Portal.
- Provides a graphical interface to interact with Blob containers, file shares, queues, and tables directly from your browser.
- Allows you to upload, download, edit, and delete data without installing additional software.
- Useful for quick access and management of storage resources within the Azure Portal.
- Supports role-based access control (RBAC) and integrates with Azure security features.

# Azure Blob Storage
- **Azure Blob Storage** is a massively scalable object storage solution for unstructured data such as text, images, videos, and backups.
- Supports storing large amounts of data for a variety of scenarios, including serving documents, streaming media, and storing backup and archival data.
- Data is organized in containers within a storage account.
- Supports three access tiers: Hot (frequent access), Cool (infrequent access), and Archive (rare access, lowest cost).
- Provides strong consistency, high availability, and durability.
- Integrates with Azure Active Directory and shared access signatures (SAS) for secure access.
- Supports REST APIs, SDKs, and Azure CLI for management and data operations.
- Storing data for backup, restore, disaster recovery, and archiving.
- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Streaming video and audio.
- Storing data for analysis by on-premises or Azure-hosted services.


# Azure Files and Azure File Sync
## Azure Files
- **Azure Files** provides fully managed file shares in the cloud that can be accessed via the SMB and NFS protocols.
- File shares can be mounted concurrently by cloud or on-premises deployments.
- Supports integration with Azure Active Directory (Azure AD) and on-premises Active Directory Domain Services (AD DS) for access control.
- File sharing across applications and users
- Lift-and-shift of legacy applications
- Centralized file storage for distributed teams

## Azure File Sync
- **Azure File Sync** enables you to centralize your organization's file shares in Azure Files while keeping the flexibility, performance, and compatibility of an on-premises file server.
- Syncs files between on-premises Windows Servers and Azure file shares.
- Supports multi-site sync, cloud tiering, and fast disaster recovery.
- Frequently accessed files are cached locally, while infrequently accessed files are stored in Azure.
- Replace or supplement on-premises file servers
- Enable hybrid file sharing scenarios
- Reduce on-premises storage footprint

# Azure Migrate
- **Azure Migrate** is a centralized hub for discovering, assessing, and migrating on-premises servers, databases, applications, anddata to Azure.
- Supports migration of VMware, Hyper-V, physical servers, databases, web apps, and virtual desktops.
- Provides tools for assessment of readiness, cost estimation, and migration planning.
- Integrated tools for server, database, and application migration.
- Assessment of on-premises workloads for Azure compatibility and sizing.
- Dependency analysis to identify application components and interdependencies.
- End-to-end tracking and management of migration projects.
- Data center modernization and cloud adoption.
- Migrating legacy applications and workloads to Azure.
- Consolidating infrastructure for cost savings and improved scalability.
- Disaster recovery and business continuity planning.

# Azure Data Box
- **Azure Data Box** is a family of physical devices and solutions designed to help transfer large amounts of data to and from Azureefficiently and securely.
- Useful when network bandwidth is limited, or transferring data over the internet would be too slow or costly.
- Provides secure, tamper-resistant devices (Data Box, Data Box Disk, Data Box Heavy) for offline data transfer.
- Supports encrypted data transfer with automatic erasure of data from the device after upload.
- Integrates with Azure Storage for seamless data ingestion.
- Large-scale data migration to Azure (e.g., backups, archives, media libraries).
- Initial bulk data transfer for cloud adoption or disaster recovery.
- Moving data from remote or disconnected locations where network transfer is impractical.
- Exporting large datasets from Azure for offline use or compliance.

# AzCopy
- **AzCopy** is a command-line utility designed for fast and reliable data transfer to and from Azure Storage.
- Supports copying data to and from Azure Blob Storage, Azure Files, and between storage accounts.
- High-performance, parallelized data transfer for large files and datasets.
- Supports authentication with Azure AD, shared access signatures (SAS), and storage account keys.
- Enables recursive copy, sync, and remove operations.
- Cross-platform support (Windows, Linux, macOS).
- Bulk upload or download of files to Azure Storage.
- Synchronizing local folders with Azure Blob containers or file shares.
- Automating backup and migration tasks using scripts.
- Transferring data between Azure storage accounts or regions.


# Azure Storage Redundancy Options
Azure provides multiple redundancy options to ensure data durability and high availability, protecting against hardware failures, data center outages, and regional disasters.
- **Locally Redundant Storage (LRS)**: Replicates data three times within a single data center in a region. Protects against local hardware failures.
- **Zone-Redundant Storage (ZRS)**: Replicates data synchronously across three Azure availability zones in a region. Protects against data center failures within a region.
- **Geo-Redundant Storage (GRS)**: Replicates data to a secondary region hundreds of miles away from the primary region, in addition to local replication. Provides disaster recovery in case of regional outages.
- **Read-Access Geo-Redundant Storage (RA-GRS)**: Same as GRS, but also allows read access to the data in the secondary region.
- **Geo-Zone-Redundant Storage (GZRS)**: Combines ZRS and GRS by replicating data across zones in the primary region and asynchronously to a secondary region.
- **Read-Access Geo-Zone-Redundant Storage (RA-GZRS)**: Same as GZRS, with read access to the secondary region.


# Azure Storage Account Types
- **General-purpose v2 (GPv2)**  
    - Most common and recommended type for most scenarios.
    - Supports all Azure storage services: blobs, files, queues, and tables.
    - Offers all redundancy options and access tiers.
    - Supports both standard and premium performance tiers.
- **General-purpose v1 (GPv1)**  
    - Legacy account type.
    - Supports blobs, files, queues, and tables.
    - Limited features and pricing flexibility compared to GPv2.
    - Not recommended for new deployments.

- **Blob Storage Account**  
    - Specialized for storing unstructured object data (blobs).
    - Supports hot and cool access tiers at the account level.
    - Does not support file shares, queues, or tables.
    - Now largely replaced by GPv2 accounts.

- **BlockBlobStorage Account**  
    - Premium performance tier for block blobs only.
    - Optimized for high transaction rates and low latency.
    - Does not support page blobs, append blobs, or other storage services.

- **FileStorage Account**  
    - Premium performance tier for Azure Files only.
    - Optimized for high IOPS and low latency file shares.
    - Does not support blobs, queues, or tables.
