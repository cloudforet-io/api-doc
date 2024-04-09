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






    
<br>

### enable





> **POST** /identity/v2/agent/enable
>






    
<br>

### disable





> **POST** /identity/v2/agent/disable
>






    
<br>

### regenerate





> **POST** /identity/v2/agent/regenerate
>






    
<br>

### delete





> **POST** /identity/v2/agent/delete
>






    
<br>

### get





> **POST** /identity/v2/agent/get
>






    
<br>

### list





> **POST** /identity/v2/agent/list
>






    


<br>
<br>

## Message



### AgentInfo
* **agent_id** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **client_secret** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
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
