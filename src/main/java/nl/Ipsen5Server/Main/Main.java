package nl.Ipsen5Server.Main;


import java.util.ArrayList;
import java.util.EnumSet;

import javax.servlet.DispatcherType;
import javax.servlet.FilterRegistration;

import io.dropwizard.jdbi3.JdbiFactory;
import io.dropwizard.server.DefaultServerFactory;
import nl.Ipsen5Server.Data.BatchDAO;
import nl.Ipsen5Server.Data.MessageDAO;
import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Dump;
import nl.Ipsen5Server.Presentation.BatchResource;
import nl.Ipsen5Server.Presentation.MessageResource;
import nl.Ipsen5Server.Interfaces.Authorisation;
import nl.Ipsen5Server.Presentation.UserResource;
import nl.Ipsen5Server.Service.Token;

import org.eclipse.jetty.servlets.CrossOriginFilter;

import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;
import org.jdbi.v3.core.Jdbi;

public class Main extends Application<Settings>{
	
	
    public static void main(String[] args) throws Exception {
        new Main().run(args);
    }
	

    @Override
    public void initialize(Bootstrap<Settings> bootstrap) {

    }
    

    @Override
    public void run(Settings settings, Environment environment) throws Exception {

        //standard database initalaizations
        final JdbiFactory factory = new JdbiFactory();
        final DefaultServerFactory serverFactory = (DefaultServerFactory) settings.getServerFactory();
        final Jdbi jdbi = factory.build(environment, settings.getDataSourceFactory(), "mariadb");

        //api prefix
        serverFactory.setApplicationContextPath("/");
        serverFactory.setJerseyRootPath("/api");

    	 // Enable CORS headers
        final FilterRegistration.Dynamic cors = environment.servlets().addFilter("CORS", CrossOriginFilter.class);
        
        // Configure CORS parameters
        cors.setInitParameter("allowedOrigins", "*");
        cors.setInitParameter("allowedHeaders", "X-Requested-With,Content-Type,Accept,Origin");
        cors.setInitParameter("allowedMethods", "OPTIONS,GET,PUT,POST,DELETE,HEAD");
        
        // Add URL mapping
        cors.addMappingForUrlPatterns(EnumSet.allOf(DispatcherType.class), true, "/*");
        
        //initialize DAO's for the resources
        final UserDAO userDAO = jdbi.onDemand(UserDAO.class);
        final MessageDAO messageDAO = jdbi.onDemand(MessageDAO.class);
        final BatchDAO batchDAO = jdbi.onDemand(BatchDAO.class);

        
        Authorisation a =  new Token();// forces you to use the interfaced method
        
        //test code here =>
     
  /*      Dump[] f = new Dump[] {new Dump("assas", "assas", "assas", "sss")} ;
        
        
      String token = "eyJhbGciOiJIUzUxMiJ9.eyJFbWFpbCI6Imsud2Fra2VybWFubUBtZWRlcndlcmtlci5ja20ubmwiLCJVc2VyUGFzc3dvcmQiOiJkb2VlZW5kYW5zamUiLCJDcmVhdGVEYXRlIjp7InllYXIiOjIwMjAsImRheU9mTW9udGgiOjI3LCJkYXlPZldlZWsiOjMsImRheU9mWWVhciI6MTQ4LCJlcmEiOjEsInllYXJPZkNlbnR1cnkiOjIwLCJjZW50dXJ5T2ZFcmEiOjIwLCJ3ZWVrT2ZXZWVreWVhciI6MjIsIndlZWt5ZWFyIjoyMDIwLCJ5ZWFyT2ZFcmEiOjIwMjAsIm1pbnV0ZU9mSG91ciI6NSwiaG91ck9mRGF5IjoxNCwibW9udGhPZlllYXIiOjUsImNocm9ub2xvZ3kiOnsiem9uZSI6eyJmaXhlZCI6dHJ1ZSwiaWQiOiJVVEMifX0sIm1pbGxpc09mU2Vjb25kIjozOTIsIm1pbGxpc09mRGF5Ijo1MDc0MzM5Miwic2Vjb25kT2ZNaW51dGUiOjQzLCJmaWVsZHMiOlt7ImxlbmllbnQiOmZhbHNlLCJyYW5nZUR1cmF0aW9uRmllbGQiOm51bGwsImxlYXBEdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjg2NDAwMDAwLCJwcmVjaXNlIjp0cnVlLCJuYW1lIjoiZGF5cyIsInR5cGUiOnsibmFtZSI6ImRheXMifSwic3VwcG9ydGVkIjp0cnVlfSwibWluaW11bVZhbHVlIjotMjkyMjc1MDU0LCJtYXhpbXVtVmFsdWUiOjI5MjI3ODk5MywiZHVyYXRpb25GaWVsZCI6eyJ1bml0TWlsbGlzIjozMTU1Njk1MjAwMCwicHJlY2lzZSI6ZmFsc2UsIm5hbWUiOiJ5ZWFycyIsInR5cGUiOnsibmFtZSI6InllYXJzIn0sInN1cHBvcnRlZCI6dHJ1ZX0sIm5hbWUiOiJ5ZWFyIiwidHlwZSI6eyJyYW5nZUR1cmF0aW9uVHlwZSI6bnVsbCwiZHVyYXRpb25UeXBlIjp7Im5hbWUiOiJ5ZWFycyJ9LCJuYW1lIjoieWVhciJ9LCJzdXBwb3J0ZWQiOnRydWV9LHsibGVuaWVudCI6ZmFsc2UsInJhbmdlRHVyYXRpb25GaWVsZCI6eyJ1bml0TWlsbGlzIjozMTU1Njk1MjAwMCwicHJlY2lzZSI6ZmFsc2UsIm5hbWUiOiJ5ZWFycyIsInR5cGUiOnsibmFtZSI6InllYXJzIn0sInN1cHBvcnRlZCI6dHJ1ZX0sImxlYXBEdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjg2NDAwMDAwLCJwcmVjaXNlIjp0cnVlLCJuYW1lIjoiZGF5cyIsInR5cGUiOnsibmFtZSI6ImRheXMifSwic3VwcG9ydGVkIjp0cnVlfSwibWluaW11bVZhbHVlIjoxLCJtYXhpbXVtVmFsdWUiOjEyLCJkdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjI2Mjk3NDYwMDAsInByZWNpc2UiOmZhbHNlLCJuYW1lIjoibW9udGhzIiwidHlwZSI6eyJuYW1lIjoibW9udGhzIn0sInN1cHBvcnRlZCI6dHJ1ZX0sIm5hbWUiOiJtb250aE9mWWVhciIsInR5cGUiOnsicmFuZ2VEdXJhdGlvblR5cGUiOnsibmFtZSI6InllYXJzIn0sImR1cmF0aW9uVHlwZSI6eyJuYW1lIjoibW9udGhzIn0sIm5hbWUiOiJtb250aE9mWWVhciJ9LCJzdXBwb3J0ZWQiOnRydWV9LHsicmFuZ2VEdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjI2Mjk3NDYwMDAsInByZWNpc2UiOmZhbHNlLCJuYW1lIjoibW9udGhzIiwidHlwZSI6eyJuYW1lIjoibW9udGhzIn0sInN1cHBvcnRlZCI6dHJ1ZX0sIm1pbmltdW1WYWx1ZSI6MSwibWF4aW11bVZhbHVlIjozMSwibGVuaWVudCI6ZmFsc2UsInVuaXRNaWxsaXMiOjg2NDAwMDAwLCJkdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjg2NDAwMDAwLCJwcmVjaXNlIjp0cnVlLCJuYW1lIjoiZGF5cyIsInR5cGUiOnsibmFtZSI6ImRheXMifSwic3VwcG9ydGVkIjp0cnVlfSwibmFtZSI6ImRheU9mTW9udGgiLCJ0eXBlIjp7InJhbmdlRHVyYXRpb25UeXBlIjp7Im5hbWUiOiJtb250aHMifSwiZHVyYXRpb25UeXBlIjp7Im5hbWUiOiJkYXlzIn0sIm5hbWUiOiJkYXlPZk1vbnRoIn0sInN1cHBvcnRlZCI6dHJ1ZSwibGVhcER1cmF0aW9uRmllbGQiOm51bGx9LHsicmFuZ2VEdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjg2NDAwMDAwLCJwcmVjaXNlIjp0cnVlLCJuYW1lIjoiZGF5cyIsInR5cGUiOnsibmFtZSI6ImRheXMifSwic3VwcG9ydGVkIjp0cnVlfSwicmFuZ2UiOjg2NDAwMDAwLCJtYXhpbXVtVmFsdWUiOjg2Mzk5OTk5LCJsZW5pZW50IjpmYWxzZSwidW5pdE1pbGxpcyI6MSwibWluaW11bVZhbHVlIjowLCJkdXJhdGlvbkZpZWxkIjp7Im5hbWUiOiJtaWxsaXMiLCJ0eXBlIjp7Im5hbWUiOiJtaWxsaXMifSwic3VwcG9ydGVkIjp0cnVlLCJ1bml0TWlsbGlzIjoxLCJwcmVjaXNlIjp0cnVlfSwibmFtZSI6Im1pbGxpc09mRGF5IiwidHlwZSI6eyJyYW5nZUR1cmF0aW9uVHlwZSI6eyJuYW1lIjoiZGF5cyJ9LCJkdXJhdGlvblR5cGUiOnsibmFtZSI6Im1pbGxpcyJ9LCJuYW1lIjoibWlsbGlzT2ZEYXkifSwic3VwcG9ydGVkIjp0cnVlLCJsZWFwRHVyYXRpb25GaWVsZCI6bnVsbH1dLCJmaWVsZFR5cGVzIjpbeyJyYW5nZUR1cmF0aW9uVHlwZSI6bnVsbCwiZHVyYXRpb25UeXBlIjp7Im5hbWUiOiJ5ZWFycyJ9LCJuYW1lIjoieWVhciJ9LHsicmFuZ2VEdXJhdGlvblR5cGUiOnsibmFtZSI6InllYXJzIn0sImR1cmF0aW9uVHlwZSI6eyJuYW1lIjoibW9udGhzIn0sIm5hbWUiOiJtb250aE9mWWVhciJ9LHsicmFuZ2VEdXJhdGlvblR5cGUiOnsibmFtZSI6Im1vbnRocyJ9LCJkdXJhdGlvblR5cGUiOnsibmFtZSI6ImRheXMifSwibmFtZSI6ImRheU9mTW9udGgifSx7InJhbmdlRHVyYXRpb25UeXBlIjp7Im5hbWUiOiJkYXlzIn0sImR1cmF0aW9uVHlwZSI6eyJuYW1lIjoibWlsbGlzIn0sIm5hbWUiOiJtaWxsaXNPZkRheSJ9XSwidmFsdWVzIjpbMjAyMCw1LDI3LDUwNzQzMzkyXX19.ac7Z6S7LdOAiviKnruXdgM6VPgQ7P9wQn7vc6KQojX9VROL2OBppJVbd-nxBG1HssMa17LhWcqJfSTZfRyeScg";
    	
        
        
        new BatchResource(batchDAO, a, userDAO).uploadDump(f, token);*/
        
        
        //Initialize new resources
        environment.jersey().register(new UserResource(userDAO, a) );
        environment.jersey().register(new MessageResource(messageDAO));
        environment.jersey().register(new BatchResource(batchDAO, a, userDAO) );

    }
}