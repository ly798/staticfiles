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