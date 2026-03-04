package org.example.utils;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.util.Date;
import java.util.Map;

/**
 * JWT 令牌操作工具类
 */
public class JwtUtils {

    // 密钥，与原测试类保持一致
    private static final String SIGN_KEY = "Znpr";
    
    // 有效期设置：12小时 (12 * 60 * 60 * 1000 毫秒)
    private static final Long EXPIRE_TIME = 43200000L;

    /**
     * 生成 JWT 令牌
     * @param claims 载荷数据（想要存储在 Token 中的信息，如 id, username）
     * @return 生成的 JWT 字符串
     */
    public static String generateJwt(Map<String, Object> claims) {
        return Jwts.builder()
                .addClaims(claims) // 设置载荷
                .signWith(SignatureAlgorithm.HS256, SIGN_KEY) // 设置签名算法和密钥
                .setExpiration(new Date(System.currentTimeMillis() + EXPIRE_TIME)) // 设置过期时间
                .compact();
    }

    /**
     * 解析 JWT 令牌
     * @param jwt JWT 字符串
     * @return 解析后的载荷数据（Claims）
     */
    public static Claims parseJwt(String jwt) {
        return Jwts.parser()
                .setSigningKey(SIGN_KEY) // 指定密钥
                .parseClaimsJws(jwt)     // 解析令牌
                .getBody();
    }
}