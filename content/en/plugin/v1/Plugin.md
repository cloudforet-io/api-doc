---
title: "Plugin"
linkTitle: "Plugin"
weight: 3
bookFlatSection: true
---
# [Plugin](#Plugin)
A Plugin is a resource managing endpoints of the plugin instances deployed. If there is a plugin instance that does not work properly, the Plugin requests the Supervisor to redeploy the instance.


>  **Package : spaceone.api.plugin.v1**

<br>
<br>

## Plugin





**Plugin Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get_plugin_endpoint**](./Plugin#get_plugin_endpoint) | [PluginEndpointRequest](Plugin#pluginendpointrequest) | [PluginEndpoint](Plugin#pluginendpoint) |
| [**get_plugin_metadata**](./Plugin#get_plugin_metadata) | [PluginMetadataRequest](Plugin#pluginmetadatarequest) | [PluginMetadata](Plugin#pluginmetadata) |
| [**notify_failure**](./Plugin#notify_failure) | [PluginFailureRequest](Plugin#pluginfailurerequest) | [Empty](Plugin#empty) |



    
<br>

### get_plugin_endpoint

Gets the `endpoint` of a specific plugin instance. A Plugin returns only a single `endpoint` by determining `labels` and `priority`. If the requested plugin instance is already deployed, the `endpoint` is returned. If not, the `endpoint` is returned after deploying the plugin instance.







 {{< tabs " get_plugin_endpoint " >}}

 {{< tab "Request Example" >}}



[PluginEndpointRequest](./Plugin#pluginendpointrequest)

* **plugin_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **version** (string)  


* **labels** (Struct)  


* **upgrade_mode** (UpgradeMode)  





{{< highlight json >}}
{
   "plugin_id": "plugin-aws-sns-mon-webhook",
   "version": "1.2.2"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginEndpoint](#PLUGINENDPOINT)
* **endpoint** (string)   `Required` 

* **access_token** (string)   `Required` 

* **updated_version** (string)   `Required` 



{{< highlight json >}}
{
   "endpoint": "grpc://endpoint-url:50051"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get_plugin_metadata





> **POST** /plugin/v1/plugin/get-plugin-metadata
>






    
<br>

### notify_failure










    


<br>
<br>

## Message



### PluginEndpoint
* **endpoint** (string)   `Required` 

    
* **access_token** (string)   `Required` 

    
* **updated_version** (string)   `Required` 

    <br>

### PluginEndpointRequest
* **plugin_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **version** (string)  

    
* **labels** (Struct)  

    
* **upgrade_mode** (UpgradeMode)  

    <br>

### PluginFailureRequest
* **supervisor_id** (string)   `Required` 

    
* **plugin_id** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### PluginMetadata
* **metadata** (Struct)   `Required` 

    <br>

### PluginMetadataRequest
* **plugin_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **version** (string)  

    
* **options** (Struct)  

    
* **upgrade_mode** (UpgradeMode)  

    <br>
