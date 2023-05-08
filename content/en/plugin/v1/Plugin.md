---
title: "Plugin"
linkTitle: "Plugin"
weight: 3
bookFlatSection: true
---
# [Plugin](#Plugin)
desc: A Plugin is a resource managing endpoints of the plugin instances deployed. If there is a plugin instance that does not work properly, the Plugin requests the Supervisor to redeploy the instance.


>  **Package : spaceone.api.plugin.v1**

<br>
<br>

## Plugin


**Plugin Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get_plugin_endpoint**](./Plugin#get_plugin_endpoint) | [PluginEndpointRequest](Plugin#pluginendpointrequest) | [PluginEndpoint](./Plugin#pluginendpoint) |
| [**notify_failure**](./Plugin#notify_failure) | [PluginFailureRequest](Plugin#pluginfailurerequest) | [Empty](./Plugin#empty) |



    
<br>

### get_plugin_endpoint

> **POST** /plugin/v1/plugin/get-plugin-endpoint
>




 {{< tabs " get_plugin_endpoint " >}}




{{< /tabs >}}

    
<br>

### notify_failure

> **POST** /plugin/v1/plugin/notify-failure
>




 {{< tabs " notify_failure " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### PluginEndpoint
* **endpoint** (string)  `Required` 

    
* **access_token** (string)  `Required` 

    
* **updated_version** (string)  `Required` 

    <br>

### PluginEndpointRequest
* **plugin_id** (string)  `Required` 

  *is_required: true*

    
* **version** (string)  `Required` 

  *is_required: false*

    
* **labels** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **upgrade_mode** (UpgradeMode)  `Required` 

  *is_required: false*

    <br>

### PluginFailureRequest
* **supervisor_id** (string)  `Required` 

  *is_required: true*

    
* **plugin_id** (string)  `Required` 

  *is_required: true*

    
* **version** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
