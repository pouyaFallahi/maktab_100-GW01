--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin; Type: TABLE; Schema: public; Owner: pouya
--

CREATE TABLE public.admin (
    admin_name character varying(15) NOT NULL,
    username character varying(100),
    password character varying(100)
);


ALTER TABLE public.admin OWNER TO pouya;

--
-- Name: docter; Type: TABLE; Schema: public; Owner: pouya
--

CREATE TABLE public.docter (
    docter_id integer NOT NULL,
    docter_name character varying(150),
    docter_age integer,
    working_day character varying(100),
    salary integer NOT NULL
);


ALTER TABLE public.docter OWNER TO pouya;

--
-- Name: patient; Type: TABLE; Schema: public; Owner: pouya
--

CREATE TABLE public.patient (
    patient_id integer NOT NULL,
    patient_name character varying(150) NOT NULL,
    patient_age integer NOT NULL,
    patient_cos integer
);


ALTER TABLE public.patient OWNER TO pouya;

--
-- Name: patient_file; Type: TABLE; Schema: public; Owner: pouya
--

CREATE TABLE public.patient_file (
    file_id integer NOT NULL,
    patient_id integer,
    docter_id integer,
    data_timevisit timestamp without time zone,
    patient_history text
);


ALTER TABLE public.patient_file OWNER TO pouya;

--
-- Name: visit; Type: TABLE; Schema: public; Owner: pouya
--

CREATE TABLE public.visit (
    visit_id integer NOT NULL,
    patient_id integer NOT NULL,
    docter_id integer NOT NULL,
    date_visit timestamp without time zone,
    order_visit text,
    cost_visit integer
);


ALTER TABLE public.visit OWNER TO pouya;

--
-- Name: docter docter_pkey; Type: CONSTRAINT; Schema: public; Owner: pouya
--

ALTER TABLE ONLY public.docter
    ADD CONSTRAINT docter_pkey PRIMARY KEY (docter_id);


--
-- Name: patient_file patient_file_pkey; Type: CONSTRAINT; Schema: public; Owner: pouya
--

ALTER TABLE ONLY public.patient_file
    ADD CONSTRAINT patient_file_pkey PRIMARY KEY (file_id);


--
-- Name: patient patient_pkey; Type: CONSTRAINT; Schema: public; Owner: pouya
--

ALTER TABLE ONLY public.patient
    ADD CONSTRAINT patient_pkey PRIMARY KEY (patient_id);


--
-- Name: visit visit_pkey; Type: CONSTRAINT; Schema: public; Owner: pouya
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT visit_pkey PRIMARY KEY (visit_id);


--
-- Name: patient_file docter_id; Type: FK CONSTRAINT; Schema: public; Owner: pouya
--

ALTER TABLE ONLY public.patient_file
    ADD CONSTRAINT docter_id FOREIGN KEY (docter_id) REFERENCES public.docter(docter_id);


--
-- Name: visit docter_id; Type: FK CONSTRAINT; Schema: public; Owner: pouya
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT docter_id FOREIGN KEY (docter_id) REFERENCES public.docter(docter_id);


--
-- Name: patient_file patient_id; Type: FK CONSTRAINT; Schema: public; Owner: pouya
--

ALTER TABLE ONLY public.patient_file
    ADD CONSTRAINT patient_id FOREIGN KEY (patient_id) REFERENCES public.patient(patient_id);


--
-- Name: visit patient_id; Type: FK CONSTRAINT; Schema: public; Owner: pouya
--

ALTER TABLE ONLY public.visit
    ADD CONSTRAINT patient_id FOREIGN KEY (patient_id) REFERENCES public.patient(patient_id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT ALL ON SCHEMA public TO pouya;


--
-- PostgreSQL database dump complete
--

