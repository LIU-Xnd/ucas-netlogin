# UCAS Network Portal Automatic Login

(For Linux Version)

## Get Project Files

```bash
$ git clone https://github.com/LIU-Xnd/ucas-netlogin.git
$ cd ucas-netlogin/

```

### Install Chrome

You can find the latest ChromeDriver on its official download page.

Install it so that a binary is located in `/usr/bin/chromedriver`

### ~~Download chromedriver (deprecated)~~

~~Download chromedriver binary from its official page, so that a binary is located at `./lib/chromedriver`.~~

Update: Some OS might automatically update Chrome so a version incompatibility might occur. The latest solution is to let selenium package handle this version compatibility. That means you have to connect to the internet manually first, and run this script, letting it install correct version of driver.

### Configure User Info

Replace information in `./data/config` into yours.

### Get Started

```bash
export ucas-netlogin(){
    before_wd=$(pwd);
    cd ~/ucas-netlogin/ && ./ucas-netlogin && cd $before_wd
}

$ ucas-netlogin
```
