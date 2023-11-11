---
title: "Handler"
linkTitle: "Handler"
weight: 3
bookFlatSection: true
---
# [Handler](#Handler)



>  **Package : spaceone.api.core.v2**

<br>
<br>

## Handler







<br>
<br>

## Message



### AuthenticationRequest
* **domain_id** (string)   `Required` 

    <br>

### AuthenticationResponse
* **domain_id** (string)   `Required` 

    
* **public_key** (string)   `Required` 

    <br>

### AuthorizationRequest
* **service** (string)   `Required` 

    
* **resource** (string)   `Required` 

    
* **verb** (string)   `Required` 

    
* **scope** (Scope)   `Required` 

    
* **require_domain_id** (bool)   `Required` 

    
* **require_workspace_id** (bool)   `Required` 

    
* **require_project_id** (bool)   `Required` 

    
* **require_user_id** (bool)   `Required` 

    
* **request_domain_id** (string)   `Required` 

    
* **request_workspace_id** (string)   `Required` 

    
* **request_project_id** (string)   `Required` 

    
* **request_user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    <br>

### AuthorizationResponse
* **role_type** (RoleType)   `Required` 

    
* **projects** (string)  `Repeated`    `Required` 

    
* **project_groups** (string)  `Repeated`    `Required` 

    <br>

### EventRequest
* **service** (string)   `Required` 

    
* **resource** (string)   `Required` 

    
* **verb** (string)   `Required` 

    
* **status** (string)   `Required` 

    
* **message** (Struct)   `Required` 

    <br>
