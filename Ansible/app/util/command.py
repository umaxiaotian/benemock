#!/usr/bin/python3.9

# -*- coding: utf-8 -*-
import logging
import subprocess
from . import log

class exec:
    # 標準出力、標準エラー出力を返す関数
    def cmd(command):
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #returnコード0以外が正常値として取得される可能性があるので、何も入力がstderrになければ
            if result.stderr == b"":
                #stderrがなければ
                log.write.info(f"[{result.returncode}] [{command}] [{result.stdout}]")
            else:
                #stderrが有効であれあ
                log.write.error(f"[{result.returncode}] [{command}] [{result.stderr}]")
            return result
        except Exception as e:
            log.write.warning(f"An exception error has occurred : {e}")
            exit(1)
        
    #変数を自前のselfに格納し、ドッド演算子で参照できるようにする
    def __init__(self,command):
        cmd_res = exec.cmd(command)
        self.returncode = cmd_res.returncode
        self.stdout = cmd_res.stdout.decode('utf-8')
        self.stderr = cmd_res.stderr.decode('utf-8')



