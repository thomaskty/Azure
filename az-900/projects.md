# Step 1. Pick a scenario that excites you

Compute services shine when you need to run code, host an app, or scale workloads. Some realistic but lightweight scenarios you could build:

- **Deploy a personal portfolio or blog** → host it with **App Service (PaaS)** or a **VM (IaaS)**.  
- **Create a serverless backend** → build an API with **Azure Functions**, hook it to a database, and test scaling.  
- **Containerize something** → put a simple app in a **Docker container**, then deploy it to **Azure Kubernetes Service (AKS)** or **Azure Container Instances (ACI)**.  
- **Data crunching job** → process a CSV or images with a **VM scale set** or **Batch**.  

The point isn’t size, but realism: it should solve something useful for you (even if tiny).

---

# Step 2. Start with one service, then expand

Instead of scattering across all compute services, try this ladder approach:

1. **IaaS (Virtual Machine):** Spin up a Linux/Windows VM, install Nginx or Apache, and serve a static website. That teaches provisioning, networking, and cost control.  
2. **PaaS (App Service):** Deploy the same site using App Service. Notice the difference in management effort.  
3. **Serverless (Functions):** Add a contact form that triggers an Azure Function and writes data to a storage account.  
4. **Containers:** Take that site, put it in a Docker image, run it locally, then push it to ACI or AKS.  

By layering this way, you *feel* the differences between the models, not just memorize them.

---

# Step 3. Add realism

- Tie your app to **Azure Storage** (for files), **Cosmos DB** (for data), or **Key Vault** (for secrets).  
- Use **Azure Monitor** or **Application Insights** to see how it behaves in real time.  
- Experiment with **scaling rules** (auto-scale App Service or VM scale sets).  

---

# Step 4. Keep it affordable

- Always pick the **free tier** or the smallest SKU.  
- **Shut down VMs** when not in use.  
- Use **Azure Cost Management** to track expenses.  
