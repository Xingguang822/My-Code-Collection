package org.example;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RequestController {

    @RequestMapping("/request")
    public String request(HttpServletRequest request){
        String method = request.getMethod();
        System.out.println("method:"+method);

        String url = request.getRequestURL().toString();
        System.out.println("url:"+url);
        String uri = request.getRequestURI().toString();
        System.out.println("uri:"+uri);

        String protocol = request.getProtocol();
        System.out.println("protocol:"+protocol);

        String name=request.getParameter("name");
        System.out.println("name:"+name);

        String accept = request.getHeader("accept");
        System.out.println("accept:"+accept);

        return "ok";
    }
}
