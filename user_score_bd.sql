toc.dat                                                                                             0000600 0004000 0002000 00000012510 14706446024 0014445 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP                        	    |            MusicScores    15.8    15.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         �           0    0 
   STDSTRINGS 
   STDSTRINGS     )   SET standard_conforming_strings = 'off';
                      false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         �           1262    56342628    MusicScores    DATABASE     �   CREATE DATABASE "MusicScores" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru_RU.UTF-8' TABLESPACE = bd5;
    DROP DATABASE "MusicScores";
                postgres    false         �            1259    56346454    history_score    TABLE     {  CREATE TABLE public.history_score (
    id integer NOT NULL,
    h_user character varying(50) NOT NULL,
    description text,
    summation boolean DEFAULT true NOT NULL,
    old_value smallint DEFAULT 0 NOT NULL,
    new_value smallint DEFAULT 0 NOT NULL,
    create_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP(0),
    value_change smallint DEFAULT 0 NOT NULL
);
 !   DROP TABLE public.history_score;
       public         heap    postgres    false         �            1259    56346453    history_score_id_seq    SEQUENCE     �   CREATE SEQUENCE public.history_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.history_score_id_seq;
       public          postgres    false    217         �           0    0    history_score_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.history_score_id_seq OWNED BY public.history_score.id;
          public          postgres    false    216         �            1259    56343327    users_scores    TABLE     �   CREATE TABLE public.users_scores (
    "user" character varying(50) NOT NULL,
    score smallint DEFAULT 0 NOT NULL,
    id integer NOT NULL
);
     DROP TABLE public.users_scores;
       public         heap    postgres    false         �            1259    56344185    users_scores_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_scores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.users_scores_id_seq;
       public          postgres    false    214         �           0    0    users_scores_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.users_scores_id_seq OWNED BY public.users_scores.id;
          public          postgres    false    215         A           2604    56346457    history_score id    DEFAULT     t   ALTER TABLE ONLY public.history_score ALTER COLUMN id SET DEFAULT nextval('public.history_score_id_seq'::regclass);
 ?   ALTER TABLE public.history_score ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216    217         @           2604    56344186    users_scores id    DEFAULT     r   ALTER TABLE ONLY public.users_scores ALTER COLUMN id SET DEFAULT nextval('public.users_scores_id_seq'::regclass);
 >   ALTER TABLE public.users_scores ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214         �          0    56346454    history_score 
   TABLE DATA           |   COPY public.history_score (id, h_user, description, summation, old_value, new_value, create_date, value_change) FROM stdin;
    public          postgres    false    217       3293.dat �          0    56343327    users_scores 
   TABLE DATA           9   COPY public.users_scores ("user", score, id) FROM stdin;
    public          postgres    false    214       3290.dat �           0    0    history_score_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.history_score_id_seq', 40, true);
          public          postgres    false    216         �           0    0    users_scores_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.users_scores_id_seq', 28, true);
          public          postgres    false    215         H           2606    56346628    users_scores user 
   CONSTRAINT     a   ALTER TABLE ONLY public.users_scores
    ADD CONSTRAINT "user" UNIQUE ("user") INCLUDE ("user");
 =   ALTER TABLE ONLY public.users_scores DROP CONSTRAINT "user";
       public            postgres    false    214         J           2606    56344191    users_scores users_scores_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.users_scores
    ADD CONSTRAINT users_scores_pkey PRIMARY KEY (id, "user");
 H   ALTER TABLE ONLY public.users_scores DROP CONSTRAINT users_scores_pkey;
       public            postgres    false    214    214         K           2606    56445445    history_score user    FK CONSTRAINT     �   ALTER TABLE ONLY public.history_score
    ADD CONSTRAINT "user" FOREIGN KEY (h_user) REFERENCES public.users_scores("user") ON DELETE CASCADE NOT VALID;
 >   ALTER TABLE ONLY public.history_score DROP CONSTRAINT "user";
       public          postgres    false    214    3144    217                                                                                                                                                                                                3293.dat                                                                                            0000600 0004000 0002000 00000000005 14706446024 0014254 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           3290.dat                                                                                            0000600 0004000 0002000 00000000005 14706446024 0014251 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           restore.sql                                                                                         0000600 0004000 0002000 00000011701 14706446024 0015373 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 15.8
-- Dumped by pg_dump version 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET escape_string_warning = off;
SET row_security = off;

DROP DATABASE "MusicScores";
--
-- Name: MusicScores; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "MusicScores" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru_RU.UTF-8' TABLESPACE = bd5;


ALTER DATABASE "MusicScores" OWNER TO postgres;

\connect "MusicScores"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET escape_string_warning = off;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: history_score; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.history_score (
    id integer NOT NULL,
    h_user character varying(50) NOT NULL,
    description text,
    summation boolean DEFAULT true NOT NULL,
    old_value smallint DEFAULT 0 NOT NULL,
    new_value smallint DEFAULT 0 NOT NULL,
    create_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP(0),
    value_change smallint DEFAULT 0 NOT NULL
);


ALTER TABLE public.history_score OWNER TO postgres;

--
-- Name: history_score_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.history_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.history_score_id_seq OWNER TO postgres;

--
-- Name: history_score_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.history_score_id_seq OWNED BY public.history_score.id;


--
-- Name: users_scores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_scores (
    "user" character varying(50) NOT NULL,
    score smallint DEFAULT 0 NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.users_scores OWNER TO postgres;

--
-- Name: users_scores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_scores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_scores_id_seq OWNER TO postgres;

--
-- Name: users_scores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_scores_id_seq OWNED BY public.users_scores.id;


--
-- Name: history_score id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_score ALTER COLUMN id SET DEFAULT nextval('public.history_score_id_seq'::regclass);


--
-- Name: users_scores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_scores ALTER COLUMN id SET DEFAULT nextval('public.users_scores_id_seq'::regclass);


--
-- Data for Name: history_score; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.history_score (id, h_user, description, summation, old_value, new_value, create_date, value_change) FROM stdin;
\.
COPY public.history_score (id, h_user, description, summation, old_value, new_value, create_date, value_change) FROM '$$PATH$$/3293.dat';

--
-- Data for Name: users_scores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_scores ("user", score, id) FROM stdin;
\.
COPY public.users_scores ("user", score, id) FROM '$$PATH$$/3290.dat';

--
-- Name: history_score_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.history_score_id_seq', 40, true);


--
-- Name: users_scores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_scores_id_seq', 28, true);


--
-- Name: users_scores user; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_scores
    ADD CONSTRAINT "user" UNIQUE ("user") INCLUDE ("user");


--
-- Name: users_scores users_scores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_scores
    ADD CONSTRAINT users_scores_pkey PRIMARY KEY (id, "user");


--
-- Name: history_score user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_score
    ADD CONSTRAINT "user" FOREIGN KEY (h_user) REFERENCES public.users_scores("user") ON DELETE CASCADE NOT VALID;


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               