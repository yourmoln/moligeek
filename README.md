<h1 align="center">MoliGeek</h1>

<p align="center">一款逐渐完善的python集成工具,努力为开发者提供最大的便利</p>
<!-- PROJECT SHIELDS -->

<p align="center">
<img src="https://img.shields.io/github/contributors/yourmoln/moligeek.svg?style=flat-square">
<img src="https://img.shields.io/github/forks/yourmoln/moligeek.svg?style=flat-square">
<img src="https://img.shields.io/github/stars/yourmoln/moligeek.svg?style=flat-square">
<img src="https://img.shields.io/github/issues/yourmoln/moligeek.svg?style=flat-square">
<a href="https://github.com/yourmoln/moligeek/blob/main/LICENSE"><img src="https://img.shields.io/github/license/yourmoln/moligeek.svg?style=flat-square"></a>
</p>

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/yourmoln/moligeek">
    <img src="https://raw.githubusercontent.com/yourmoln/moligeek/main/logo.ico" alt="Logo">
  </a>

  <h3 align="center">moligeek</h3>
  <p align="center">
    打造最完善的python工具!
    <br />
    <a href="https://github.com/yourmoln/moligeek#%E7%9B%AE%E5%BD%95"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://www.bilibili.com/video/BV1vG411P79B/">查看Demo</a>
    ·
    <a href="https://github.com/yourmoln/moligeek/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=%5BBug%5D%E6%88%91%E5%8F%91%E7%8E%B0%E4%B8%80%E4%B8%AA%E6%96%B0%E7%9A%84Bug%3A">报告Bug</a>
    ·
    <a href="https://github.com/yourmoln/moligeek/issues/new?assignees=&labels=help+wanted&projects=&template=feature_request.md&title=%5BFeature+Request%5D%E6%88%91%E6%9C%89%E4%B8%80%E4%B8%AA%E6%96%B0%E7%9A%84%E5%8A%9F%E8%83%BD%E5%BB%BA%E8%AE%AE%3A">提出新特性</a>
  </p>

</p>
 
 
<h2>目录</h2>

- [运行环境安装](#运行环境安装)
  - [Termux](#termux)
  - [Windows](#windows)
  - [Linux](#linux)
- [使用需求](#使用需求)
  - [现有功能](#现有功能)
  - [开发环境](#开发环境)
  - [如何参与开源项目](#如何参与开源项目)
  - [作者](#作者)
  - [版权说明](#版权说明)
  - [特别鸣谢](#特别鸣谢)

## 运行环境安装

### Termux
**快速安装**  
1.Termux可依次运行以下指令进行安装
```
apt install python
pip install moligeek
```
2.输入moligeek开始运行
```
moliggk
```

**传统安装**  
1.Termux可依次运行以下指令进行安装
```
apt install python
apt install git
git clone https://github.com/yourmoln/moligeek.git
```
2.安装完成后可用以下指令运行
```
python ./moligeek/main.py
```
3.若安装过程出现意外，请使用以下指令换源后重新尝试以上指令
```
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list
apt update && apt upgrade
```
### Windows
**以下为三种不同的安装方式**
1. 在本仓库的[releases](https://github.com/yourmoln/moligeek/releases)下载windows版本的moligeek
2. 如果Windows版本高于16299(Windows 10 1709)并且软件包安装程序为最新版本，可尝试使用Winget命令安装moligeek
```
winget install moligeek
```
3. 使用python运行本仓库的源代码
---

### Linux



**Debian & Ubuntu**

```sh
apt install python
```

**CentOS**

```sh
yum install python
```

## 使用需求

**快速安装**

```sh
pip install moligeek
```

输入moligeek直接运行即可

**传统安装**

1. 安装脚本

```sh
git clone https://github.com/yourmoln/moligeek.git
```

2. 运行脚本

```sh
python ./moligeek/main.py
```

请在项目根目录下运行该指令

### 现有功能
1. 下载源码  
2. 提交表单  
3. 后台扫描  
4. dos攻击   
5. zip破解  
6. 密文处理  
持续更新中...  

### 开发环境

[python](https://python.org)

**依赖**

- 请在[requirements.txt](https://github.com/yourmoln/moligeek/blob/main/requirements.txt)查看
- ps:脚本运行时会自动安装缺失依赖


### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request


### 作者

[yourmoln](https://github.com/yourmoln)

qq交流群:564136017    

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 [LICENSE.txt](https://github.com/yourmoln/moligeek/blob/main/LICENSE)

### 特别鸣谢


- [miaobuao](https://github.com/miaobuao)
- [CoolPlayLin](https://github.com/CoolPlayLin)



<!-- links -->
[your-project-path]:yourmoln/moligeek
[contributors-shield]: https://img.shields.io/github/contributors/yourmoln/moligeek.svg?style=flat-square
[contributors-url]: https://github.com/yourmoln/moligeek/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/yourmoln/moligeek.svg?style=flat-square
[forks-url]: https://github.com/yourmoln/moligeek/network/members
[stars-shield]: https://img.shields.io/github/stars/yourmoln/moligeek.svg?style=flat-square
[stars-url]: https://github.com/yourmoln/moligeek/stargazers
[issues-shield]: https://img.shields.io/github/issues/yourmoln/moligeek.svg?style=flat-square
[issues-url]: https://github.com/yourmoln/moligeek/issues
[license-shield]: https://img.shields.io/github/license/yourmoln/moligeek.svg?style=flat-square
[license-url]: https://github.com/yourmoln/moligeek/blob/main/LICENSE




