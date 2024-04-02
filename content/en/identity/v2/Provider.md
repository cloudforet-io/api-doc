---
title: "Provider"
linkTitle: "Provider"
weight: 3
bookFlatSection: true
---
# [Provider](#Provider)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Provider





**Provider Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Provider#create) | [CreateProviderRequest](Provider#createproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**update**](./Provider#update) | [UpdateProviderRequest](Provider#updateproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**update_plugin**](./Provider#update_plugin) | [UpdatePluginProviderRequest](Provider#updatepluginproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**delete**](./Provider#delete) | [ProviderRequest](Provider#providerrequest) | [Empty](Provider#empty) |
| [**get**](./Provider#get) | [ProviderRequest](Provider#providerrequest) | [ProviderInfo](Provider#providerinfo) |
| [**list**](./Provider#list) | [ProviderSearchQuery](Provider#providersearchquery) | [ProvidersInfo](Provider#providersinfo) |
| [**stat**](./Provider#stat) | [ProviderStatQuery](Provider#providerstatquery) | [Struct](Provider#struct) |



    
<br>

### create





> **POST** /identity/v2/provider/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateProviderRequest](./Provider#createproviderrequest)

* **provider** (string)   `Required` 


* **name** (string)   `Required` 


* **alias** (string)  


* **plugin_info** (PluginInfo)  

  *If plugin_info is not empty, your provider support trusted account and support auto sync for Cloudforet.
These two options are located in options field. not in plugin_info.*


* **color** (string)  


* **icon** (string)  


* **order** (int32)  


* **options** (Struct)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "provider": "aws",
 "name": "AWS",
 "alias": "AWS",
 "color": "#FF9900",
 "icon": "https://cloudforet.io/icons/aws.svg",
 "order": 1,
 "options": {
      "supported_trusted_account": false
 }
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/provider/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateProviderRequest](./Provider#updateproviderrequest)

* **provider** (string)   `Required` 


* **name** (string)  


* **alias** (string)  


* **plugin_info** (PluginInfo)  


* **color** (string)  


* **icon** (string)  


* **order** (int32)  


* **options** (Struct)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "provider": "aws",
 "name": "AWS",
 "alias": "AWS",
 "color": "#FF9900",
 "icon": "https://cloudforet.io/icons/aws.svg",
 "order": 2,
 "options": {
      "supported_trusted_account": false
 },
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update_plugin





> **POST** /identity/v2/provider/update-plugin
>





 {{< tabs " update_plugin " >}}

 {{< tab "Request Example" >}}



[UpdatePluginProviderRequest](./Provider#updatepluginproviderrequest)

* **provider** (string)   `Required` 

  *Managed provider are aws, azure, google_cloud and kubernetes. Maybe more in the future.*


* **version** (string)  


* **options** (Struct)  


* **upgrade_mode** (UpgradeMode)  





{{< highlight json >}}
{
 "provider": "aws",
 "version": "1.0.0",
 "options": {},
 "upgrade_mode": "AUTO"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/provider/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[ProviderRequest](./Provider#providerrequest)

* **provider** (string)   `Required` 





{{< highlight json >}}
{
 "provider": "aws"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/provider/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[ProviderRequest](./Provider#providerrequest)

* **provider** (string)   `Required` 





{{< highlight json >}}
{
 "provider": "aws"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/provider/list
>






    
<br>

### stat





> **POST** /identity/v2/provider/stat
>






    


<br>
<br>

## Message



### CreateProviderRequest
* **provider** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **alias** (string)  

    
* **plugin_info** (PluginInfo)  

  *If plugin_info is not empty, your provider support trusted account and support auto sync for Cloudforet.
These two options are located in options field. not in plugin_info.*

    
* **color** (string)  

    
* **icon** (string)  

    
* **order** (int32)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### PluginInfo
* **plugin_id** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **upgrade_mode** (UpgradeMode)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **metadata** (Struct)   `Required` 

    <br>

### ProviderInfo
* **provider** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **alias** (string)   `Required` 

    
* **plugin_info** (PluginInfo)   `Required` 

    
* **color** (string)   `Required` 

    
* **icon** (string)   `Required` 

    
* **order** (int32)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### ProviderRequest
* **provider** (string)   `Required` 

    <br>

### ProviderSearchQuery
* **query** (Query)  

    
* **provider** (string)  

    
* **name** (string)  

    
* **alias** (string)  

    
* **is_managed** (bool)  

    <br>

### ProviderStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ProvidersInfo
* **results** (ProviderInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePluginProviderRequest
* **provider** (string)   `Required` 

  *Managed provider are aws, azure, google_cloud and kubernetes. Maybe more in the future.*

    
* **version** (string)  

    
* **options** (Struct)  

    
* **upgrade_mode** (UpgradeMode)  

    <br>

### UpdateProviderRequest
* **provider** (string)   `Required` 

    
* **name** (string)  

    
* **alias** (string)  

    
* **plugin_info** (PluginInfo)  

    
* **color** (string)  

    
* **icon** (string)  

    
* **order** (int32)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
