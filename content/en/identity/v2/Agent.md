---
title: "Agent"
linkTitle: "Agent"
weight: 3
bookFlatSection: true
---
# [Agent](#Agent)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Agent

Create Agent with service account , Currently only Kubernetes service account is supported for OpenCost



**Agent Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Agent#create) | [CreateAgentRequest](Agent#createagentrequest) | [AgentInfo](Agent#agentinfo) |
| [**enable**](./Agent#enable) | [AgentRequest](Agent#agentrequest) | [AgentInfo](Agent#agentinfo) |
| [**disable**](./Agent#disable) | [AgentRequest](Agent#agentrequest) | [AgentInfo](Agent#agentinfo) |
| [**regenerate**](./Agent#regenerate) | [AgentRequest](Agent#agentrequest) | [AgentInfo](Agent#agentinfo) |
| [**delete**](./Agent#delete) | [AgentRequest](Agent#agentrequest) | [Empty](Agent#empty) |
| [**get**](./Agent#get) | [AgentRequest](Agent#agentrequest) | [AgentInfo](Agent#agentinfo) |
| [**list**](./Agent#list) | [AgentSearchQuery](Agent#agentsearchquery) | [AgentsInfo](Agent#agentsinfo) |



    
<br>

### create





> **POST** /identity/v2/agent/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateAgentRequest](./Agent#createagentrequest)

* **service_account_id** (string)   `Required` 


* **options** (Struct)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a120f6d21c4e",
 "options": {
   "cluster_name": "k8s-prd-cluster",
   "kube_state_metrics": "false",
   "prometheus_node_exporter": "false"
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AgentInfo](#AGENTINFO)
* **agent_id** (string)   `Required` 

* **options** (Struct)   `Required` 

* **client_secret** (string)   `Required` 

* **state** (State)   `Required` 

* **is_managed** (bool)   `Required` 

* **role_type** (RoleType)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **app_id** (string)   `Required` 

* **role_id** (string)   `Required` 

* **client_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **expired_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
   "agent_id": "agent-5cb52dc61c70",
   "options": {
       "kube_state_metrics": false,
       "cluster_name": "k8s-prd-cluster",
       "prometheus_node_exporter": false
   },
   "client_secret": "client_secret_from_app",
   "state": "ENABLED",
   "is_managed": true,
   "role_type": "WORKSPACE_OWNER",
   "domain_id": "domain-116226a1516a",
   "workspace_id": "workspace-7a0aebcf4eb2",
   "project_id": "project-441975c8dfd8",
   "service_account_id": "sa-a120f6d21c4e",
   "app_id": "app-aa7bf47c98ea",
   "role_id": "managed-workspace-owner",
   "client_id": "client-36e1034b3512",
   "created_at": "2024-11-13T00:34:09.125Z",
   "expired_at": "2025-11-13T00:34:09.000Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable





> **POST** /identity/v2/agent/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[AgentRequest](./Agent#agentrequest)

* **service_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a120f6d21c4e"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AgentInfo](#AGENTINFO)
* **agent_id** (string)   `Required` 

* **options** (Struct)   `Required` 

* **client_secret** (string)   `Required` 

* **state** (State)   `Required` 

* **is_managed** (bool)   `Required` 

* **role_type** (RoleType)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **app_id** (string)   `Required` 

* **role_id** (string)   `Required` 

* **client_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **expired_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
   "agent_id": "agent-5cb52dc61c70",
   "options": {
       "kube_state_metrics": false,
       "cluster_name": "k8s-prd-cluster",
       "prometheus_node_exporter": false
   },
   "client_secret": "client_secret_from_app",
   "state": "ENABLED",
   "is_managed": true,
   "role_type": "WORKSPACE_OWNER",
   "domain_id": "domain-116226a1516a",
   "workspace_id": "workspace-7a0aebcf4eb2",
   "project_id": "project-441975c8dfd8",
   "service_account_id": "sa-a120f6d21c4e",
   "app_id": "app-aa7bf47c98ea",
   "role_id": "managed-workspace-owner",
   "client_id": "client-36e1034b3512",
   "created_at": "2024-11-13T00:34:09.125Z",
   "expired_at": "2025-11-13T00:34:09.000Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable





> **POST** /identity/v2/agent/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[AgentRequest](./Agent#agentrequest)

* **service_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a120f6d21c4e"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AgentInfo](#AGENTINFO)
* **agent_id** (string)   `Required` 

* **options** (Struct)   `Required` 

* **client_secret** (string)   `Required` 

* **state** (State)   `Required` 

* **is_managed** (bool)   `Required` 

* **role_type** (RoleType)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **app_id** (string)   `Required` 

* **role_id** (string)   `Required` 

* **client_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **expired_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
   "agent_id": "agent-5cb52dc61c70",
   "options": {
       "kube_state_metrics": false,
       "cluster_name": "k8s-prd-cluster",
       "prometheus_node_exporter": false
   },
   "client_secret": "client_secret_from_app",
   "state": "ENABLED",
   "is_managed": true,
   "role_type": "WORKSPACE_OWNER",
   "domain_id": "domain-116226a1516a",
   "workspace_id": "workspace-7a0aebcf4eb2",
   "project_id": "project-441975c8dfd8",
   "service_account_id": "sa-a120f6d21c4e",
   "app_id": "app-aa7bf47c98ea",
   "role_id": "managed-workspace-owner",
   "client_id": "client-36e1034b3512",
   "created_at": "2024-11-13T00:34:09.125Z",
   "expired_at": "2025-11-13T00:34:09.000Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### regenerate





> **POST** /identity/v2/agent/regenerate
>





 {{< tabs " regenerate " >}}

 {{< tab "Request Example" >}}



[AgentRequest](./Agent#agentrequest)

* **service_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a120f6d21c4e"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AgentInfo](#AGENTINFO)
* **agent_id** (string)   `Required` 

* **options** (Struct)   `Required` 

* **client_secret** (string)   `Required` 

* **state** (State)   `Required` 

* **is_managed** (bool)   `Required` 

* **role_type** (RoleType)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **app_id** (string)   `Required` 

* **role_id** (string)   `Required` 

* **client_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **expired_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
   "agent_id": "agent-5cb52dc61c70",
   "options": {
       "kube_state_metrics": false,
       "cluster_name": "k8s-prd-cluster",
       "prometheus_node_exporter": false
   },
   "client_secret": "client_secret_from_app",
   "state": "ENABLED",
   "is_managed": true,
   "role_type": "WORKSPACE_OWNER",
   "domain_id": "domain-116226a1516a",
   "workspace_id": "workspace-7a0aebcf4eb2",
   "project_id": "project-441975c8dfd8",
   "service_account_id": "sa-a120f6d21c4e",
   "app_id": "app-aa7bf47c98ea",
   "role_id": "managed-workspace-owner",
   "client_id": "client-36e1034b3512",
   "created_at": "2024-11-13T00:34:09.125Z",
   "expired_at": "2025-11-13T00:34:09.000Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/agent/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[AgentRequest](./Agent#agentrequest)

* **service_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a120f6d21c4e"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/agent/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[AgentRequest](./Agent#agentrequest)

* **service_account_id** (string)   `Required` 





{{< highlight json >}}
{
 "service_account_id": "sa-a120f6d21c4e"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AgentInfo](#AGENTINFO)
* **agent_id** (string)   `Required` 

* **options** (Struct)   `Required` 

* **client_secret** (string)   `Required` 

* **state** (State)   `Required` 

* **is_managed** (bool)   `Required` 

* **role_type** (RoleType)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **app_id** (string)   `Required` 

* **role_id** (string)   `Required` 

* **client_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **expired_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
   "agent_id": "agent-5cb52dc61c70",
   "options": {
       "kube_state_metrics": false,
       "cluster_name": "k8s-prd-cluster",
       "prometheus_node_exporter": false
   },
   "client_secret": "client_secret_from_app",
   "state": "ENABLED",
   "is_managed": true,
   "role_type": "WORKSPACE_OWNER",
   "domain_id": "domain-116226a1516a",
   "workspace_id": "workspace-7a0aebcf4eb2",
   "project_id": "project-441975c8dfd8",
   "service_account_id": "sa-a120f6d21c4e",
   "app_id": "app-aa7bf47c98ea",
   "role_id": "managed-workspace-owner",
   "client_id": "client-36e1034b3512",
   "created_at": "2024-11-13T00:34:09.125Z",
   "expired_at": "2025-11-13T00:34:09.000Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/agent/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[AgentSearchQuery](./Agent#agentsearchquery)

* **query** (Query)  


* **agent_id** (string)  


* **service_account_id** (string)  


* **state** (State)  





{{< highlight json >}}
{
 "query": {
   "page": {
     "start":1,
     "limit": 10
   }
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AgentsInfo](#AGENTSINFO)
* **results** (AgentInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
   {
     "agent_id": "agent-5cb52dc61c70",
     "options": {
       "kube_state_metrics": false,
       "cluster_name": "k8s-prd-cluster",
       "prometheus_node_exporter": false
     },
     "client_secret": "client_secret_from_app",
     "state": "ENABLED",
     "is_managed": true,
     "role_type": "WORKSPACE_OWNER",
     "domain_id": "domain-116226a1516a",
     "workspace_id": "workspace-7a0aebcf4eb2",
     "project_id": "project-441975c8dfd8",
     "service_account_id": "sa-a120f6d21c4e",
     "app_id": "app-aa7bf47c98ea",
     "role_id": "managed-workspace-owner",
     "client_id": "client-36e1034b3512",
     "created_at": "2024-11-13T00:34:09.125Z",
     "expired_at": "2025-11-13T00:34:09.000Z"
   }
 ],
 "total_count": 1
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### AgentInfo
* **agent_id** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **client_secret** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **app_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **client_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **expired_at** (string)   `Required` 

    
* **last_accessed_at** (string)   `Required` 

    <br>

### AgentRequest
* **service_account_id** (string)   `Required` 

    <br>

### AgentSearchQuery
* **query** (Query)  

    
* **agent_id** (string)  

    
* **service_account_id** (string)  

    
* **state** (State)  

    <br>

### AgentsInfo
* **results** (AgentInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateAgentRequest
* **service_account_id** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    <br>
