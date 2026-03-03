package org.example.aop;

import com.google.gson.JsonObject;
import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.codehaus.jettison.json.JSONObject;
import org.example.mapper.OperateLogMapper;
import org.example.pojo.OperateLog;
import org.example.utils.CurrentHolder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.util.Arrays;

@Slf4j
@Aspect
@Component
public class LogAspect {

    @Autowired
    private OperateLogMapper operateLogMapper;

    /**
     * 环绕通知：匹配 org.example.controller 包下所有带有 @Log 注解的方法
     */
    @Around("@annotation(org.example.anno.Log)")
    public Object recordLog(ProceedingJoinPoint joinPoint) throws Throwable {
        
        // 1. 记录开始时间
        long begin = System.currentTimeMillis();

        // 2. 调用原始方法运行
        Object result = joinPoint.proceed();

        // 3. 记录结束时间并计算耗时
        long end = System.currentTimeMillis();
        long costTime = end - begin;

        // 4. 收集并组装日志信息
        OperateLog operateLog = new OperateLog();
        
        // 操作人ID：通常从 JWT 解析出来的 ThreadLocal 中获取
        // 这里假设你的工具类叫 BaseContext
        operateLog.setOperateEmpId(getCurrentId());
        
        operateLog.setOperateTime(LocalDateTime.now());
        operateLog.setClassName(joinPoint.getTarget().getClass().getName());
        operateLog.setMethodName(joinPoint.getSignature().getName());
        
        // 方法参数：转为字符串存储
        Object[] args = joinPoint.getArgs();
        operateLog.setMethodParams(Arrays.toString(args));
        
        // 返回值：转为 JSON 字符串存储
        operateLog.setReturnValue(result!=null?result.toString():"void");
        
        operateLog.setCostTime(costTime);

        // 5. 异步/同步保存日志
        operateLogMapper.insert(operateLog);

        log.info("AOP记录操作日志: {}", operateLog);

        return result;
    }

    private Integer getCurrentId() {
        return CurrentHolder.getCurrentId();
    }
}