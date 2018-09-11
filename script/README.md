script
======

### 设置 docker 的源

```
curl -sSL https://raw.githubusercontent.com/ly798/staticfiles/master/script/set_mirror.sh | sh -s https://registry.docker-cn.com
```

### 生成 kolla iptables 规则

先按照要求修改脚本参数

```
python kolla_iptables.py
```

### 设置网卡绑定(centos)

先按照要求修改脚本参数

```
python nic_bind.py
```

### trove 初始化 mysql

先上传 mysql 镜像

```
bash trove_mysql_init.sh c91582d9-c489-4714-87cb-6795c90f737e
```