package org.example;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.junit.jupiter.api.Test;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class JwtTest {

    @Test
    public void testGenerateJwt(){
        Map<String, Object> map=new HashMap<>();
        map.put("id",1);
        map.put("username",2);

        String jwt=Jwts.builder().signWith(SignatureAlgorithm.HS256,"Znpr")
                .addClaims(map)
                .setExpiration(new Date(System.currentTimeMillis()+3600*1000))
                .compact();
        System.out.println(jwt);
    }

    @Test
    public void testParseJwt(){
        String token="eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOjIsImV4cCI6MTc3MjUxNTY3OH0.L0P13vv7mWERIBS1yxJgaf94Bnced0dMSxCZ-rMsDCY";

        Claims claims=Jwts.parser().setSigningKey("Znpr").parseClaimsJws(token).getBody();
        System.out.println(claims);
    }
}
