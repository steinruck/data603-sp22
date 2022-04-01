### Abstract

As the Internet of Things (IoT) grows, the amount of data generated at any moment increases exponentially. While cloud computing is vital to the processing of this data, the sheer amount can cause issues with bandwidth capabilities, latency, scalability, security, and others. The ability to bring processing power closer to the user solves or reduces the effects of many of these problems by providing near real-time analysis using inference methods developed in the cloud and deployed to the edge. This reduces the strain on traditional computational resources, such as data centers. Where more robust cloud analysis provides thorough modeling based on large amounts of data, these edge devices can be used to implement solutions with streamlined information while receiving improvements obtained from the cloud analytic results. This seamless integration can be used to perform analysis without waiting for the data to be sent to a centralized location. This way, data can be filtered before it gets to the data stores instead of having to comb through enormous amounts of data at once. This helps reduce processing strain on data management platforms and could potentially decrease long term maintenance costs. It could also help provide real time information for decision making, such as shutting down a machine when a sensor detects a part is failing rather than waiting for the data to be processed after it is stored. Because analysis happens at or near the source, there is lower latency and network connectivity isn't necessary for immediate results. In addition, since data can be filtered at the source, only relevant data, whether it be images, sensor readings, or video, needs to be transmitted, saving bandwidth and space. This is especially relevant in places with less reliable connectivity. This paper discusses both cloud and edge technologies, why edge computing is beneficial, as well as some real-world use cases to demonstrate effectiveness.


## Introduction
The IoT is constantly growing. As more devices become available that provide a wide variety of functions, the decision to use the collected data to streamline efficiency comes naturally. IoT devices generate a large amount of data that can be analyzed in real-time or offline to improve productivity. In order to do this, the data needs to be stored and managed in a way that provides convenient access and robust capabilities. This can be accomplished using a combination of edge and cloud computing. In this way, the edge devices provide the real-time analysis and computation while the cloud computing provides storage and resource intensive analytic capabilities. Implemented correctly, “by reducing the distance between where data is collected and where it’s processed, organizations can react quickly to real-time insights, unlocking that potential.” [<sup>4</sup>](#resource-list) 
 - 5 vs of big data
  - volume - amount of data. Data at rest. 
  - velocity - speed data moves. Data in motion.
  - variety - range of data types and sources.
  - veracity - uncertainty of data
  - value - TCO and ROI of data


## Cloud vs Edge
- Cloud: Data is external to your network and accessed over HTTP. Computation and software resources are available on demand with less required hardware and administration efforts. Have monthly subscription costs and might required skilled administrators or engineers to maintain. 


**Figure 1**

*What is Cloud Computing*

<img src ="https://www.frontiersin.org/files/Articles/587139/fdata-03-587139-HTML-r1/image_m/fdata-03-587139-g001.jpg" width="50%">

*Note.* From *Frontiers* article on Securing Machine Learning in the Cloud.[<sup>5</sup>](#resource-list)

- Edge: Access Data at the Edge of your Network or from the Device. Computation, control, and command is local. Used in robotics, smart machines, self driving cars. Are often mobile but require an independent power supply. There are tradeoffs between computation power, consumtion, and data storage capacity.


**Figure 2**

*What is Edge Computing*

<img src = "https://blogs.nvidia.com/wp-content/uploads/2019/10/edge-computing-infrastructure.png" align="center" width="50%">

*Note.* From NVIDIA blog on Edge Computing by Tiffany Yeung. October 22, 2019. [<sup>8</sup>](#resource-list)


**Figure 1**

*Integrated Cloud and Edge*

<img src = "https://upload.wikimedia.org/wikipedia/commons/b/bf/Edge_computing_infrastructure.png" align="center" width="50%">

*Note.* Integration of cloud and edge computing from Wikipedia.[<sup>7</sup>](#resource-list)



**Figure 3**
*Cloud and Edge Comparison*

<img src = "https://smart-it.io/wp-content/uploads/2019/12/Cloud-Computing-and-Edge-Computing-Compared-1189x2048.jpg.webp" width="40%">

*Note.* Table depicting the key difference between cloud and edge computing.[<sup>3</sup>](#resource-list) 

## Benefits of Edge Computing
NVIDIA lists 5 benefits to edge computing. Two of the most important are:
> Lower Latency: Since edge devices are located where data is generated or collected, latency is greatly reduced. Data doesn't need to be sent back to data centers or to the cloud, so analysis and prediction can be completed in real-time. This analysis can include activities like instantly alerting factory workers when a machine malfunctions. "With this on-thespot insight into their data, enterprises can optimize operations, boost safety in manufacturing, accelerate disease diagnosis, (and) improve customer experiences with faster services" all while avoiding infrastructure restrictions like storage and transmission resources.[<sup>4</sup>](#resource-list) 

**Figure 4**
*Data Latency by Distance*

![image](https://user-images.githubusercontent.com/42300445/161169423-df04b28c-84be-49d2-ad65-7952584a6d6f.png)

*Note.* Table from DATA690 Applied Artificial Intelligence Lecture 1.5.


> Scalability: Standard cloud solutions run the risk of limited bandwidth which can lead to higher costs. Edge computing removes the need for transmition of data to the cloud, since collection and processing happens on the local network. 

## Edge Computing in Practice
Including but not limited to:
- Autonomous Vehicles: Immediate reaction to hazards can't wait for instruction from a remote server. Vehicles using edge technology can communicate with each other first to share information critical to safety.
- Healthcare: Wearable health devices can instantly alert caregivers, robots in surgery can analyze data in real-time to help with decision making. 
- Security: Surveillance and security systems can identify and alert on threats near instantaniously without first needing to transmit video streams or sensor data to a remote location. This is especially useful with systems like Closed Circuit Television (CCTV) systems that are on-premises.
- Advertising: Everyone is familiar with targeted ads, especially on social media. Edge devices can help improve privacy by encrypting data before it reaches the cloud.
- Personal Assistants : Smart speakers can  interpret voice instructions and perform basic tasks, like controlling the light, temperature, or music. Edge computing allows these actions to be performed even with no network connection.
- Video Conferencing: Video faces many issues from quality, delay, dropped frames, or audio delays. "By placing the server-side of video conferencing software closer to participants, quality problems can be reduced."[<sup>2</sup>](#resource-list)
- Real time video analytics 
<img src="https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/9739/9102343/8976180/han11-2970550-small.gif">

**Figure 4**

*Edge Computing Real-World Examples*

<img src = "https://innovationatwork.ieee.org/wp-content/uploads/2019/06/Real-Life-Use-Cases-for-Edge-Computing_1024X684.png" width="50%">

*Note.* Basic examples of real world edge computing applications from IEEE.[<sup>2</sup>](#resource-list)

## Conclusion
- Rather than constantly transmitting and storing all data generated by the IoT, edge devices can be used to perform offline analysis and upload only data identified as relevant or low confidence predictions when a connection is established. 
- This allows for high tech solutions in less reliably connected locations while saving both time and resources. 

## <span style="color:#0c416a;">Resources:</span><a class="anchor" id="resource-list"></a>
1.  
2. IEEE. (2019, August 26). Real-life use cases for Edge Computing. IEEE Innovation at Work. Retrieved March 30, 2022, from https://innovationatwork.ieee.org/real-life-edge-computing-use-cases/ 
3. Kaplunou, P. (2019, December 27). Cloud computing and Edge Computing compared [infographic]. Smart IT. Retrieved March 22, 2022, from https://smart-it.io/blog/cloud-computing-vs-edge-computing-infographic/ 
4. NVIDIA. (2021, June). TOP CONSIDERATIONS FOR DEPLOYING AI AT THE EDGE. Nvidia : Top considerations for deploying AI at the edge. Retrieved March 17, 2022, from https://app.hushly.com/runtime/content/b8jY9yGQ2QZmDQoT  
5. Qayyum, A., Ijaz, A., Usama, M., Iqbal, W., Qadir, J., Elkhatib, Y., &amp; Al-Fuqaha, A. (1AD, January 1). Securing Machine Learning in the cloud: A systematic review of Cloud Machine Learning Security. Frontiers. Retrieved March 31, 2022, from https://www.frontiersin.org/articles/10.3389/fdata.2020.587139/full 
6. Wang, X., Han, Y., Leung, V. C., Niyato, D., Yan, X., & Chen, X. (2020). Convergence of Edge Computing and deep learning: A comprehensive survey. IEEE Communications Surveys & Tutorials, 22(2), 869–904. https://doi.org/10.1109/comst.2020.2970550 
7. Wikimedia Foundation. (2022, March 20). Edge computing. Wikipedia. Retrieved March 31, 2022, from https://en.wikipedia.org/wiki/Edge_computing 
8. Yeung, T. (2019, October 22). What is edge computing? NVIDIA Blog. Retrieved March 30, 2022, from https://blogs.nvidia.com/blog/2019/10/22/what-is-edge-computing/ 
