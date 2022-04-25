# Big Data Analysis at the Edge

## The State of Things

The Internet of Things (IoT) is constantly growing. As more devices become available that provide a wide variety of functions, the decision to use the collected data to streamline efficiency comes naturally. IoT devices generate a large amount of data that can be analyzed in real-time or offline to improve productivity. While cloud computing is vital to the processing of this data, the sheer amount can cause issues with bandwidth capabilities, latency, scalability, security, and others. The very characteristics of big data make it necessary to adjust the approach for processing it. 

<p align="center">
  <img width=50% src="https://cdn.ttgtmedia.com/rms/onlineimages/data_management-big_data_vs_02.png"></br>
  <i>Characteristics of Big Data - Image from TechTarget</i> <a href="#resource-list"><sup>1</sup></a>
</p> 

The ability to bring processing power closer to the user solves or reduces the effects of many of these problems by providing near real-time analysis using inference methods developed in the cloud and deployed to the edge. This reduces the strain on traditional computational resources, such as data centers. 

Where more robust cloud analysis provides thorough modeling based on large amounts of data, these edge devices can be used to implement solutions with streamlined information while receiving improvements obtained from the cloud analytic results. This seamless integration can be used to perform analysis without waiting for the data to be sent to a centralized location. This way, data can be filtered before it gets to the data stores instead of having to comb through enormous amounts of data at once. This helps reduce processing strain on data management platforms and could potentially decrease long term maintenance costs. It could also help provide real time information for decision making, such as shutting down a machine when a sensor detects a part is failing rather than waiting for the data to be processed after it is stored. Because analysis happens at or near the source, there is lower latency and network connectivity isn't necessary for immediate results. In addition, since data can be filtered at the source, only relevant data, whether it be images, sensor readings, or video, needs to be transmitted, saving bandwidth and space. This is especially relevant in places with less reliable connectivity.

In order to do this, the data needs to be stored and managed in a way that provides convenient access and robust capabilities. This can be accomplished using a combination of edge and cloud computing. In this way, the edge devices provide the real-time analysis and computation while the cloud computing provides storage and resource intensive analytic capabilities. Implemented correctly, “by reducing the distance between where data is collected and where it’s processed, organizations can react quickly to real-time insights, unlocking that potential.” [<sup>2</sup>](#resource-list) 

## Cloud vs Edge
Cloud computing is a pretty well known concept, but in simple terms "cloud computing means storing and accessing data and programs over the internet instead of your computer's hard drive." [<sup>3</sup>](#resource-list) There are many reasons why this is a good method in many situations, but the conversation around edge computing targets issues with latency, bandwidth, privacy, and scalability. 

> Data is external to your network and accessed over HTTP. Computation and software resources are available on demand with less required hardware and administration efforts. These usually involve monthly subscription costs and might require skilled administrators or engineers to maintain. 

<p align="center">
  <img width=50% src="https://www.frontiersin.org/files/Articles/587139/fdata-03-587139-HTML-r1/image_m/fdata-03-587139-g001.jpg"></br>
  <i>What is Cloud Computing - Image from Frontiers</i> <a href="#resource-list"><sup>4</sup></a>
</p> 

Since edge computing occurs closer to the data source, it is expected to be naturally faster in terms of processing time. Data collected by sensors or IoT devices can be processed at or close to the source without relying on an Internet connection. Only the result of that processing is transmitted once complete. 

> Data is accessed at the edge of the network or on the device. Computation, control, and command is local. Common use cases include robotics, smart machines, and self driving cars. There are tradeoffs between computation power, consumtion, and data storage capacity since the devices are usually small by design and might require a mobile power source.

<p align="center">
  <img width=60% src="https://blogs.nvidia.com/wp-content/uploads/2019/10/edge-computing-infrastructure.png"></br>
  <i>What is Edge Computing - Image from NVIDIA</i> <a href="#resource-list"><sup>5</sup></a>
</p> 

Below is a side by side comparison of cloud and edge computing. While cloud offers centralized storage of large amounts of data, remote processing, scalability, and higher security, edge offers real-time results from or near the data source using a decentalized system. There are benefits to each of them, but for now the focus is on edge computing.

<p align="center">
  <img width=50% src="https://smart-it.io/wp-content/uploads/2019/12/Cloud-Computing-and-Edge-Computing-Compared-1189x2048.jpg.webp"></br>
  <i>Cloud vs Edge - Image from Smart-IT</i> <a href="#resource-list"><sup>6</sup></a>
</p> 

## Benefits of Edge Computing
NVIDIA lists 5 benefits to edge computing. For the purposes of this discussion, two can be considered the most important.
> Lower Latency: Since edge devices are located where data is generated or collected, latency is greatly reduced. Data doesn't need to be sent back to data centers or to the cloud, so analysis and prediction can be completed in real-time. This analysis can include activities like instantly alerting factory workers when a machine malfunctions. "With this on-the spot insight into their data, enterprises can optimize operations, boost safety in manufacturing, accelerate disease diagnosis, (and) improve customer experiences with faster services" all while avoiding infrastructure restrictions like storage and transmission resources.[<sup>7</sup>](#resource-list) 

<p align="center">
  <img width=60% src="https://user-images.githubusercontent.com/42300445/161169423-df04b28c-84be-49d2-ad65-7952584a6d6f.png"></br>
  <i>Data Latency by Distance - Image from DATA690 Professor Delafuente</i> <a href="#resource-list"><sup>8</sup></a>
</p> 

> Scalability: Standard cloud solutions run the risk of limited bandwidth which can lead to higher costs. Edge computing removes the need for transmition of data to the cloud, since collection and processing happens on the local network. Edge devices are designed to be cost effective and easy to integrate into an existing network of devices, though management of an increased number of devices can be complicated without a single remote management system.  

## Integration
This isn't to say that edge computing should completely replace cloud computing. It would be borderline absurd to attempt to do so. Instead, an integration of the two technolgies would provide an environment where rapid inference can take place where needed, and further analysis can occur away from the data source when time is not a factor. This integration looks something like this:

<p align="center">
  <img width=50% src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Edge_computing_infrastructure.png"></br>
  <i>Integration of Cloud and Edge - Image from Wikipedia</i> <a href="#resource-list"><sup>9</sup></a>
</p> 

Data is processed and filtered at the edge, and only the necessary information is forwarded to the cloud for storage and further processing. This allows faster processing as well as a decrease in the amount of data stored in the cloud. This can be seen in a number of ongoing projects and fields.

## Edge Computing in Practice
There are several current projects involving the integration of cloud and edge computing. The most obvious are autonomous vehicles designed to recognize obstacles and react accordingly. There isn’t time in most cases to wait for data to be transmitted to a remote location, analyzed, and returned. Instead, trained models are deployed in the onboard computing environment and decisions are made without further contact with the cloud. Different edge devices in a single vehicle can communicate about “accidents, weather conditions, traffic, or detours”[<sup>2</sup>](#resource-list), allowing each individual device to focus on its task. 

<p align="center">
  <img width=45% src="https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/9739/9102343/8976180/han11-2970550-small.gif"></br>
  <i>Computational Levels - Image from IEEE</i> <a href="#resource-list"><sup>10</sup></a>
</p> 

In the above image, three levels are used to achieve results. The end devices capture the information that needs to be processed (video, senors data, etc.), edge devices sit near the data source and perform the inference activities. The outcome from these is then sent to the cloud, where parameters for the model can be updated for better performance. The goal is to reduce bandwith and resource consumption while providing powerful computational abilities.[<sup>10</sup>](#resource-list) 

## Conclusion

Similar methods can be used with wearable health devices, smart speakers, or even unmaned drones. With distributed computing at the edge, the opportunities for real-time analytics are endless. Edge computing isn't a replacement for traditional big data processing. With edge devices, data is collected and analyzed at or near the source, and only relevant information is passed to the cloud. This could be anything from value predictions to images labeled as relevant by the model rather than everything collected, saving time and resources in the long run. 

## <span style="color:#0c416a;">Resources:</span><a class="anchor" id="resource-list"></a>
1. Kelly, W. (2019, July 12). Cloud cost implications of the 5 V's of big data. SearchCloudComputing. Retrieved April 17, 2022, from https://www.techtarget.com/searchcloudcomputing/tip/Cost-implications-of-the-5-Vs-of-big-dat
2. IEEE. (2019, August 26). Real-life use cases for Edge Computing. IEEE Innovation at Work. Retrieved March 30, 2022, from https://innovationatwork.ieee.org/real-life-edge-computing-use-cases/
3. Griffith, E. (2022, February 15). What is cloud computing? PCMAG. Retrieved April 17, 2022, from https://www.pcmag.com/how-to/what-is-cloud-computing  
4. Qayyum, A., Ijaz, A., Usama, M., Iqbal, W., Qadir, J., Elkhatib, Y., &amp; Al-Fuqaha, A. (1AD, January 1). Securing Machine Learning in the cloud: A systematic review of Cloud Machine Learning Security. Frontiers. Retrieved March 31, 2022, from https://www.frontiersin.org/articles/10.3389/fdata.2020.587139/full 
5. Yeung, T. (2019, October 22). What is edge computing? NVIDIA Blog. Retrieved March 30, 2022, from https://blogs.nvidia.com/blog/2019/10/22/what-is-edge-computing/
6. Kaplunou, P. (2019, December 27). Cloud computing and Edge Computing compared [infographic]. Smart IT. Retrieved March 22, 2022, from https://smart-it.io/blog/cloud-computing-vs-edge-computing-infographic/ 
7. NVIDIA. (2021, June). TOP CONSIDERATIONS FOR DEPLOYING AI AT THE EDGE. Nvidia : Top considerations for deploying AI at the edge. Retrieved March 17, 2022, from https://app.hushly.com/runtime/content/b8jY9yGQ2QZmDQoT  
8. Delafuente, P. (2021). Lecture 1.5: AIoT and Big Data. 
9. Wikimedia Foundation. (2022, March 20). Edge computing. Wikipedia. Retrieved March 31, 2022, from https://en.wikipedia.org/wiki/Edge_computing
10. Wang, X., Han, Y., Leung, V. C., Niyato, D., Yan, X., & Chen, X. (2020). Convergence of Edge Computing and deep learning: A comprehensive survey. IEEE Communications Surveys & Tutorials, 22(2), 869–904. https://doi.org/10.1109/comst.2020.2970550 
 



