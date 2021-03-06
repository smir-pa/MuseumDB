PGDMP     5    1        
        x            Museum    12.0    12.0 ~    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24576    Museum    DATABASE     �   CREATE DATABASE "Museum" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE "Museum";
                postgres    false            �           0    0    DATABASE "Museum"    ACL     	  GRANT CONNECT ON DATABASE "Museum" TO fund_worker;
GRANT CONNECT ON DATABASE "Museum" TO security_worker;
GRANT CONNECT ON DATABASE "Museum" TO senior_employee;
GRANT CONNECT ON DATABASE "Museum" TO auction_participant;
GRANT CONNECT ON DATABASE "Museum" TO fedor;
                   postgres    false    3006            �           0    0    Museum    DATABASE PROPERTIES     :   ALTER DATABASE "Museum" SET lc_monetary TO 'ru_RU.UTF-8';
                     postgres    false            �            1255    74051    check_employee()    FUNCTION     �  CREATE FUNCTION public.check_employee() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF NEW.full_name IS NULL THEN
            RAISE EXCEPTION 'Full name cannot be null';
        END IF;
        IF NEW.salary IS NULL THEN
            RAISE EXCEPTION '% cannot have null salary', NEW.full_name;
        END IF;
        IF NEW.salary < 0::money THEN
            RAISE EXCEPTION '% cannot have a negative salary', NEW.full_name;
        END IF;
        IF EXTRACT(YEAR FROM NEW.date_of_birth) < 1945 OR EXTRACT(YEAR FROM NEW.date_of_birth) > 2000 THEN
            RAISE EXCEPTION '% cannot have such date of birth', NEW.full_name;
        END IF;
        RETURN NEW;
    END;
$$;
 '   DROP FUNCTION public.check_employee();
       public          postgres    false            �            1255    74124    delete_exhibit_in_location()    FUNCTION     �   CREATE FUNCTION public.delete_exhibit_in_location() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
DELETE FROM exhibit_location WHERE OLD.id = exhibit_location.exhibit_id;
RETURN OLD;
END;
$$;
 3   DROP FUNCTION public.delete_exhibit_in_location();
       public          postgres    false            �            1255    74122    delete_product_in_sale()    FUNCTION     �   CREATE FUNCTION public.delete_product_in_sale() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	DELETE FROM sale WHERE OLD.id = sale.product_id;
	RETURN OLD;
END;
$$;
 /   DROP FUNCTION public.delete_product_in_sale();
       public          postgres    false            �            1255    74111 B   make_pass(character varying, character varying, character varying)    FUNCTION     �   CREATE FUNCTION public.make_pass(usr_pass character varying, usr_name character varying, salt character varying) RETURNS character varying
    LANGUAGE plpgsql
    AS $$
BEGIN
	RETURN 'md5' || MD5(MD5(usr_pass || usr_name) || salt);
END
$$;
 p   DROP FUNCTION public.make_pass(usr_pass character varying, usr_name character varying, salt character varying);
       public          postgres    false            �            1259    32855    auction    TABLE     �   CREATE TABLE public.auction (
    id integer NOT NULL,
    exhibit_id integer NOT NULL,
    seller integer NOT NULL,
    buyer integer NOT NULL,
    price money NOT NULL,
    date date NOT NULL
);
    DROP TABLE public.auction;
       public         heap    postgres    false            �           0    0    TABLE auction    ACL     =   GRANT SELECT ON TABLE public.auction TO auction_participant;
          public          postgres    false    210            �            1255    74110    show_auction()    FUNCTION     �   CREATE FUNCTION public.show_auction() RETURNS SETOF public.auction
    LANGUAGE sql
    AS $$
	SET lc_monetary TO "ru_RU.UTF-8";
	SELECT * FROM auction;
$$;
 %   DROP FUNCTION public.show_auction();
       public          postgres    false    210            �            1259    32821    employee    TABLE     �   CREATE TABLE public.employee (
    id integer NOT NULL,
    full_name character varying NOT NULL,
    date_of_birth date NOT NULL,
    post character varying NOT NULL,
    salary money NOT NULL
);
    DROP TABLE public.employee;
       public         heap    postgres    false            �           0    0    TABLE employee    ACL     O   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.employee TO senior_employee;
          public          postgres    false    206            �            1255    74109    show_employee()    FUNCTION     �   CREATE FUNCTION public.show_employee() RETURNS SETOF public.employee
    LANGUAGE sql
    AS $$
	SET lc_monetary TO "ru_RU.UTF-8";
	SELECT * FROM employee;
$$;
 &   DROP FUNCTION public.show_employee();
       public          postgres    false    206            �            1259    32829 	   excursion    TABLE     <  CREATE TABLE public.excursion (
    id integer NOT NULL,
    "time" time(6) without time zone NOT NULL,
    schedule character varying NOT NULL,
    "end" date NOT NULL,
    guide integer NOT NULL,
    price money NOT NULL,
    name character varying NOT NULL,
    hall integer NOT NULL,
    master_class integer
);
    DROP TABLE public.excursion;
       public         heap    postgres    false            �           0    0    TABLE excursion    ACL     P   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.excursion TO senior_employee;
          public          postgres    false    207            �            1255    74108    show_excursion()    FUNCTION     �   CREATE FUNCTION public.show_excursion() RETURNS SETOF public.excursion
    LANGUAGE sql
    AS $$
	SET lc_monetary TO "ru_RU.UTF-8";
	SELECT * FROM excursion;
$$;
 '   DROP FUNCTION public.show_excursion();
       public          postgres    false    207            �            1259    32850    exhibit_purchase    TABLE     �   CREATE TABLE public.exhibit_purchase (
    id integer NOT NULL,
    exhibit_id integer NOT NULL,
    price money NOT NULL,
    date_of_purchase date NOT NULL,
    fund integer NOT NULL
);
 $   DROP TABLE public.exhibit_purchase;
       public         heap    postgres    false            �           0    0    TABLE exhibit_purchase    ACL     S   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.exhibit_purchase TO fund_worker;
          public          postgres    false    209            �            1255    74107    show_exhibit_purchase()    FUNCTION     �   CREATE FUNCTION public.show_exhibit_purchase() RETURNS SETOF public.exhibit_purchase
    LANGUAGE sql
    AS $$
	SET lc_monetary TO "ru_RU.UTF-8";
	SELECT * FROM exhibit_purchase;
$$;
 .   DROP FUNCTION public.show_exhibit_purchase();
       public          postgres    false    209            �            1259    32908 	   financing    TABLE       CREATE TABLE public.financing (
    id integer NOT NULL,
    sponsor character varying NOT NULL,
    date_of_financing date NOT NULL,
    amount_of_money money NOT NULL,
    phone_number character varying NOT NULL,
    fund integer NOT NULL,
    email character varying
);
    DROP TABLE public.financing;
       public         heap    postgres    false            �           0    0    TABLE financing    ACL     L   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.financing TO fund_worker;
          public          postgres    false    215            �            1255    74106    show_financing()    FUNCTION     �   CREATE FUNCTION public.show_financing() RETURNS SETOF public.financing
    LANGUAGE sql
    AS $$
	SET lc_monetary TO "ru_RU.UTF-8";
	SELECT * FROM financing;
$$;
 '   DROP FUNCTION public.show_financing();
       public          postgres    false    215            �            1259    65808    sale    TABLE     �   CREATE TABLE public.sale (
    product_id integer NOT NULL,
    quantity integer NOT NULL,
    proceeds money,
    fund integer NOT NULL
);
    DROP TABLE public.sale;
       public         heap    postgres    false            �           0    0 
   TABLE sale    ACL     G   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.sale TO fund_worker;
          public          postgres    false    221            �            1255    74105    show_sale()    FUNCTION     �   CREATE FUNCTION public.show_sale() RETURNS SETOF public.sale
    LANGUAGE sql
    AS $$
	SET lc_monetary TO "ru_RU.UTF-8";
	SELECT * FROM sale;
$$;
 "   DROP FUNCTION public.show_sale();
       public          postgres    false    221            �            1259    32876    shop    TABLE     �   CREATE TABLE public.shop (
    id integer NOT NULL,
    product_name character varying NOT NULL,
    price money NOT NULL,
    manufacturer character varying NOT NULL,
    pic character varying,
    quantity integer NOT NULL
);
    DROP TABLE public.shop;
       public         heap    postgres    false            �           0    0 
   TABLE shop    ACL     G   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.shop TO fund_worker;
          public          postgres    false    212            �            1255    74104    show_shop()    FUNCTION     �   CREATE FUNCTION public.show_shop() RETURNS SETOF public.shop
    LANGUAGE sql
    AS $$
	SET lc_monetary TO "ru_RU.UTF-8";
	SELECT * FROM shop;
$$;
 "   DROP FUNCTION public.show_shop();
       public          postgres    false    212            �            1255    74102    upd_proceeds()    FUNCTION     �  CREATE FUNCTION public.upd_proceeds() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	IF TG_OP = 'UPDATE' THEN
		OLD.quantity = NEW.quantity;
		OLD.proceeds = NEW.quantity * (SELECT price FROM shop WHERE NEW.product_id = shop.id);
		RETURN OLD;
	ELSIF TG_OP = 'INSERT' THEN
		OLD.product_id = NEW.product_id;
		OLD.quantity = NEW.quantity;
		OLD.fund = NEW.fund;
		OLD.proceeds = NEW.quantity * (SELECT price FROM shop WHERE NEW.product_id = shop.id);
		RETURN OLD;
	END IF;
END;
$$;
 %   DROP FUNCTION public.upd_proceeds();
       public          postgres    false            �            1259    32868    auction_visitor    TABLE     �   CREATE TABLE public.auction_visitor (
    id integer NOT NULL,
    full_name character varying NOT NULL,
    date_of_birth date NOT NULL,
    phone_number character varying NOT NULL,
    email character varying
);
 #   DROP TABLE public.auction_visitor;
       public         heap    postgres    false            �           0    0    TABLE auction_visitor    ACL     L   GRANT SELECT,INSERT ON TABLE public.auction_visitor TO auction_participant;
          public          postgres    false    211            �            1259    32884    creation_place    TABLE     �   CREATE TABLE public.creation_place (
    creation_place_number integer NOT NULL,
    free_places integer NOT NULL,
    special_equipment character varying NOT NULL
);
 "   DROP TABLE public.creation_place;
       public         heap    postgres    false            �           0    0    TABLE creation_place    ACL     G   GRANT SELECT,UPDATE ON TABLE public.creation_place TO senior_employee;
          public          postgres    false    213            �            1259    65631    employee_workplace    TABLE     �   CREATE TABLE public.employee_workplace (
    id integer NOT NULL,
    type character varying NOT NULL,
    workplace_id integer NOT NULL,
    employee_id integer NOT NULL
);
 &   DROP TABLE public.employee_workplace;
       public         heap    postgres    false            �           0    0    TABLE employee_workplace    ACL     Y   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.employee_workplace TO senior_employee;
          public          postgres    false    218            �            1259    32900    event    TABLE     �   CREATE TABLE public.event (
    id integer NOT NULL,
    name character varying NOT NULL,
    date date NOT NULL,
    hall integer NOT NULL,
    "time" time without time zone NOT NULL
);
    DROP TABLE public.event;
       public         heap    postgres    false            �           0    0    TABLE event    ACL     L   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.event TO senior_employee;
          public          postgres    false    214            �            1259    24578    exhibit    TABLE     �   CREATE TABLE public.exhibit (
    id integer NOT NULL,
    name character varying NOT NULL,
    author character varying NOT NULL,
    pic character varying,
    date character varying,
    type character varying
);
    DROP TABLE public.exhibit;
       public         heap    postgres    false            �           0    0    TABLE exhibit    ACL     �   GRANT SELECT,INSERT ON TABLE public.exhibit TO fund_worker;
GRANT SELECT ON TABLE public.exhibit TO auction_participant;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.exhibit TO senior_employee;
          public          postgres    false    202            �            1259    65710    exhibit_location    TABLE     �   CREATE TABLE public.exhibit_location (
    exhibit_id integer NOT NULL,
    type character varying NOT NULL,
    location_id integer NOT NULL,
    place_number integer NOT NULL
);
 $   DROP TABLE public.exhibit_location;
       public         heap    postgres    false            �           0    0    TABLE exhibit_location    ACL     W   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.exhibit_location TO senior_employee;
          public          postgres    false    220            �            1259    32916    fund    TABLE     y   CREATE TABLE public.fund (
    id integer NOT NULL,
    name character varying NOT NULL,
    report character varying
);
    DROP TABLE public.fund;
       public         heap    postgres    false            �           0    0 
   TABLE fund    ACL     9   GRANT SELECT,UPDATE ON TABLE public.fund TO fund_worker;
          public          postgres    false    216            �            1259    32806    hall    TABLE     �   CREATE TABLE public.hall (
    hall_number integer NOT NULL,
    number_of_places integer NOT NULL,
    area real NOT NULL,
    number_of_exhibits integer NOT NULL,
    free_places integer NOT NULL
);
    DROP TABLE public.hall;
       public         heap    postgres    false            �           0    0 
   TABLE hall    ACL     =   GRANT SELECT,UPDATE ON TABLE public.hall TO senior_employee;
          public          postgres    false    203            �            1259    65664    master_class    TABLE     �   CREATE TABLE public.master_class (
    id integer NOT NULL,
    master_class_name character varying NOT NULL,
    result character varying NOT NULL,
    short_description character varying,
    creation_place_id integer NOT NULL
);
     DROP TABLE public.master_class;
       public         heap    postgres    false            �           0    0    TABLE master_class    ACL     S   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.master_class TO senior_employee;
          public          postgres    false    219            �            1259    32925    research_activity    TABLE     �   CREATE TABLE public.research_activity (
    id integer NOT NULL,
    name character varying NOT NULL,
    date_of_research date NOT NULL,
    author integer NOT NULL
);
 %   DROP TABLE public.research_activity;
       public         heap    postgres    false            �           0    0    TABLE research_activity    ACL     X   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.research_activity TO senior_employee;
          public          postgres    false    217            �            1259    32816    storage    TABLE     �   CREATE TABLE public.storage (
    storage_number integer NOT NULL,
    number_of_places integer NOT NULL,
    number_of_exhibits integer NOT NULL,
    free_places integer NOT NULL
);
    DROP TABLE public.storage;
       public         heap    postgres    false            �           0    0    TABLE storage    ACL     @   GRANT SELECT,UPDATE ON TABLE public.storage TO senior_employee;
          public          postgres    false    205            �            1259    32837    visitor    TABLE     �   CREATE TABLE public.visitor (
    id integer NOT NULL,
    full_name character varying NOT NULL,
    excursion integer NOT NULL,
    ticket_number integer NOT NULL
);
    DROP TABLE public.visitor;
       public         heap    postgres    false            �           0    0    TABLE visitor    ACL     9   GRANT SELECT ON TABLE public.visitor TO security_worker;
          public          postgres    false    208            �            1259    32811    workshop    TABLE     �   CREATE TABLE public.workshop (
    workshop_number integer NOT NULL,
    number_of_places integer NOT NULL,
    number_of_exhibits integer NOT NULL,
    free_places integer NOT NULL
);
    DROP TABLE public.workshop;
       public         heap    postgres    false            �           0    0    TABLE workshop    ACL     A   GRANT SELECT,UPDATE ON TABLE public.workshop TO senior_employee;
          public          postgres    false    204            �          0    32855    auction 
   TABLE DATA           M   COPY public.auction (id, exhibit_id, seller, buyer, price, date) FROM stdin;
    public          postgres    false    210   ��       �          0    32868    auction_visitor 
   TABLE DATA           \   COPY public.auction_visitor (id, full_name, date_of_birth, phone_number, email) FROM stdin;
    public          postgres    false    211   ��       �          0    32884    creation_place 
   TABLE DATA           _   COPY public.creation_place (creation_place_number, free_places, special_equipment) FROM stdin;
    public          postgres    false    213   �       �          0    32821    employee 
   TABLE DATA           N   COPY public.employee (id, full_name, date_of_birth, post, salary) FROM stdin;
    public          postgres    false    206   .�       �          0    65631    employee_workplace 
   TABLE DATA           Q   COPY public.employee_workplace (id, type, workplace_id, employee_id) FROM stdin;
    public          postgres    false    218   �       �          0    32900    event 
   TABLE DATA           =   COPY public.event (id, name, date, hall, "time") FROM stdin;
    public          postgres    false    214   ��       �          0    32829 	   excursion 
   TABLE DATA           h   COPY public.excursion (id, "time", schedule, "end", guide, price, name, hall, master_class) FROM stdin;
    public          postgres    false    207   ��       �          0    24578    exhibit 
   TABLE DATA           D   COPY public.exhibit (id, name, author, pic, date, type) FROM stdin;
    public          postgres    false    202   ̧       �          0    65710    exhibit_location 
   TABLE DATA           W   COPY public.exhibit_location (exhibit_id, type, location_id, place_number) FROM stdin;
    public          postgres    false    220   ��       �          0    32850    exhibit_purchase 
   TABLE DATA           Y   COPY public.exhibit_purchase (id, exhibit_id, price, date_of_purchase, fund) FROM stdin;
    public          postgres    false    209   �       �          0    32908 	   financing 
   TABLE DATA           o   COPY public.financing (id, sponsor, date_of_financing, amount_of_money, phone_number, fund, email) FROM stdin;
    public          postgres    false    215   q�       �          0    32916    fund 
   TABLE DATA           0   COPY public.fund (id, name, report) FROM stdin;
    public          postgres    false    216   ��       �          0    32806    hall 
   TABLE DATA           d   COPY public.hall (hall_number, number_of_places, area, number_of_exhibits, free_places) FROM stdin;
    public          postgres    false    203   S�       �          0    65664    master_class 
   TABLE DATA           k   COPY public.master_class (id, master_class_name, result, short_description, creation_place_id) FROM stdin;
    public          postgres    false    219   ��       �          0    32925    research_activity 
   TABLE DATA           O   COPY public.research_activity (id, name, date_of_research, author) FROM stdin;
    public          postgres    false    217   �       �          0    65808    sale 
   TABLE DATA           D   COPY public.sale (product_id, quantity, proceeds, fund) FROM stdin;
    public          postgres    false    221   ��       �          0    32876    shop 
   TABLE DATA           T   COPY public.shop (id, product_name, price, manufacturer, pic, quantity) FROM stdin;
    public          postgres    false    212   ��       �          0    32816    storage 
   TABLE DATA           d   COPY public.storage (storage_number, number_of_places, number_of_exhibits, free_places) FROM stdin;
    public          postgres    false    205   ��       �          0    32837    visitor 
   TABLE DATA           J   COPY public.visitor (id, full_name, excursion, ticket_number) FROM stdin;
    public          postgres    false    208   �       �          0    32811    workshop 
   TABLE DATA           f   COPY public.workshop (workshop_number, number_of_places, number_of_exhibits, free_places) FROM stdin;
    public          postgres    false    204   M�       �
           2606    32859    auction auction_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.auction
    ADD CONSTRAINT auction_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.auction DROP CONSTRAINT auction_pkey;
       public            postgres    false    210            �
           2606    32875    auction_visitor buyer_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auction_visitor
    ADD CONSTRAINT buyer_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auction_visitor DROP CONSTRAINT buyer_pkey;
       public            postgres    false    211            �
           2606    32891 "   creation_place creation_place_pkey 
   CONSTRAINT     s   ALTER TABLE ONLY public.creation_place
    ADD CONSTRAINT creation_place_pkey PRIMARY KEY (creation_place_number);
 L   ALTER TABLE ONLY public.creation_place DROP CONSTRAINT creation_place_pkey;
       public            postgres    false    213            �
           2606    32828    employee employee_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pkey;
       public            postgres    false    206                       2606    65638 *   employee_workplace employee_workplace_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.employee_workplace
    ADD CONSTRAINT employee_workplace_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.employee_workplace DROP CONSTRAINT employee_workplace_pkey;
       public            postgres    false    218            �
           2606    32907    event event_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.event DROP CONSTRAINT event_pkey;
       public            postgres    false    214            �
           2606    32836    excursion excursion_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.excursion
    ADD CONSTRAINT excursion_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.excursion DROP CONSTRAINT excursion_pkey;
       public            postgres    false    207                       2606    65806 &   exhibit_location exhibit_location_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.exhibit_location
    ADD CONSTRAINT exhibit_location_pkey PRIMARY KEY (exhibit_id);
 P   ALTER TABLE ONLY public.exhibit_location DROP CONSTRAINT exhibit_location_pkey;
       public            postgres    false    220            �
           2606    32915    financing financing_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.financing
    ADD CONSTRAINT financing_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.financing DROP CONSTRAINT financing_pkey;
       public            postgres    false    215                        2606    32923    fund fund_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.fund
    ADD CONSTRAINT fund_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.fund DROP CONSTRAINT fund_pkey;
       public            postgres    false    216            �
           2606    32810    hall hall_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.hall
    ADD CONSTRAINT hall_pkey PRIMARY KEY (hall_number);
 8   ALTER TABLE ONLY public.hall DROP CONSTRAINT hall_pkey;
       public            postgres    false    203                       2606    65671    master_class master_class_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.master_class
    ADD CONSTRAINT master_class_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.master_class DROP CONSTRAINT master_class_pkey;
       public            postgres    false    219            �
           2606    24585    exhibit picture_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.exhibit
    ADD CONSTRAINT picture_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.exhibit DROP CONSTRAINT picture_pkey;
       public            postgres    false    202            �
           2606    32854 *   exhibit_purchase purchase_of_exhibits_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.exhibit_purchase
    ADD CONSTRAINT purchase_of_exhibits_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.exhibit_purchase DROP CONSTRAINT purchase_of_exhibits_pkey;
       public            postgres    false    209                       2606    32932 (   research_activity research_activity_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.research_activity
    ADD CONSTRAINT research_activity_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.research_activity DROP CONSTRAINT research_activity_pkey;
       public            postgres    false    217            
           2606    65812    sale souvenir_sale_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.sale
    ADD CONSTRAINT souvenir_sale_pkey PRIMARY KEY (product_id);
 A   ALTER TABLE ONLY public.sale DROP CONSTRAINT souvenir_sale_pkey;
       public            postgres    false    221            �
           2606    32883    shop souvenir_shop_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.shop
    ADD CONSTRAINT souvenir_shop_pkey PRIMARY KEY (id);
 A   ALTER TABLE ONLY public.shop DROP CONSTRAINT souvenir_shop_pkey;
       public            postgres    false    212            �
           2606    32820    storage storage_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.storage
    ADD CONSTRAINT storage_pkey PRIMARY KEY (storage_number);
 >   ALTER TABLE ONLY public.storage DROP CONSTRAINT storage_pkey;
       public            postgres    false    205            �
           2606    32844    visitor visitor_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.visitor
    ADD CONSTRAINT visitor_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.visitor DROP CONSTRAINT visitor_pkey;
       public            postgres    false    208            �
           2606    32815    workshop workshop_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.workshop
    ADD CONSTRAINT workshop_pkey PRIMARY KEY (workshop_number);
 @   ALTER TABLE ONLY public.workshop DROP CONSTRAINT workshop_pkey;
       public            postgres    false    204            #           2620    74125    exhibit t_delete_exhibit    TRIGGER     �   CREATE TRIGGER t_delete_exhibit BEFORE DELETE ON public.exhibit FOR EACH ROW EXECUTE FUNCTION public.delete_exhibit_in_location();
 1   DROP TRIGGER t_delete_exhibit ON public.exhibit;
       public          postgres    false    230    202            %           2620    74123    shop t_delete_product    TRIGGER     |   CREATE TRIGGER t_delete_product BEFORE DELETE ON public.shop FOR EACH ROW EXECUTE FUNCTION public.delete_product_in_sale();
 .   DROP TRIGGER t_delete_product ON public.shop;
       public          postgres    false    245    212            $           2620    74052    employee t_employee    TRIGGER     |   CREATE TRIGGER t_employee BEFORE INSERT OR UPDATE ON public.employee FOR EACH ROW EXECUTE FUNCTION public.check_employee();
 ,   DROP TRIGGER t_employee ON public.employee;
       public          postgres    false    228    206            &           2620    74103    sale t_sale    TRIGGER     r   CREATE TRIGGER t_sale BEFORE INSERT OR UPDATE ON public.sale FOR EACH ROW EXECUTE FUNCTION public.upd_proceeds();
 $   DROP TRIGGER t_sale ON public.sale;
       public          postgres    false    221    244                       2606    65828    auction auction_buyer_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.auction
    ADD CONSTRAINT auction_buyer_fkey FOREIGN KEY (buyer) REFERENCES public.auction_visitor(id) NOT VALID;
 D   ALTER TABLE ONLY public.auction DROP CONSTRAINT auction_buyer_fkey;
       public          postgres    false    210    2806    211                       2606    33033    auction auction_exhibit_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.auction
    ADD CONSTRAINT auction_exhibit_id_fkey FOREIGN KEY (exhibit_id) REFERENCES public.exhibit(id) NOT VALID;
 I   ALTER TABLE ONLY public.auction DROP CONSTRAINT auction_exhibit_id_fkey;
       public          postgres    false    202    210    2788                       2606    65823    auction auction_seller_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.auction
    ADD CONSTRAINT auction_seller_fkey FOREIGN KEY (seller) REFERENCES public.auction_visitor(id) NOT VALID;
 E   ALTER TABLE ONLY public.auction DROP CONSTRAINT auction_seller_fkey;
       public          postgres    false    211    2806    210                       2606    65659 6   employee_workplace employee_workplace_employee_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.employee_workplace
    ADD CONSTRAINT employee_workplace_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employee(id);
 `   ALTER TABLE ONLY public.employee_workplace DROP CONSTRAINT employee_workplace_employee_id_fkey;
       public          postgres    false    2796    218    206                       2606    65639 7   employee_workplace employee_workplace_workplace_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.employee_workplace
    ADD CONSTRAINT employee_workplace_workplace_id_fkey FOREIGN KEY (workplace_id) REFERENCES public.creation_place(creation_place_number);
 a   ALTER TABLE ONLY public.employee_workplace DROP CONSTRAINT employee_workplace_workplace_id_fkey;
       public          postgres    false    218    2810    213                       2606    65644 8   employee_workplace employee_workplace_workplace_id_fkey1    FK CONSTRAINT     �   ALTER TABLE ONLY public.employee_workplace
    ADD CONSTRAINT employee_workplace_workplace_id_fkey1 FOREIGN KEY (workplace_id) REFERENCES public.hall(hall_number);
 b   ALTER TABLE ONLY public.employee_workplace DROP CONSTRAINT employee_workplace_workplace_id_fkey1;
       public          postgres    false    203    218    2790                       2606    65649 8   employee_workplace employee_workplace_workplace_id_fkey2    FK CONSTRAINT     �   ALTER TABLE ONLY public.employee_workplace
    ADD CONSTRAINT employee_workplace_workplace_id_fkey2 FOREIGN KEY (workplace_id) REFERENCES public.storage(storage_number);
 b   ALTER TABLE ONLY public.employee_workplace DROP CONSTRAINT employee_workplace_workplace_id_fkey2;
       public          postgres    false    2794    218    205                       2606    65654 8   employee_workplace employee_workplace_workplace_id_fkey3    FK CONSTRAINT     �   ALTER TABLE ONLY public.employee_workplace
    ADD CONSTRAINT employee_workplace_workplace_id_fkey3 FOREIGN KEY (workplace_id) REFERENCES public.workshop(workshop_number);
 b   ALTER TABLE ONLY public.employee_workplace DROP CONSTRAINT employee_workplace_workplace_id_fkey3;
       public          postgres    false    204    2792    218                       2606    33053    event event_hall_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_hall_fkey FOREIGN KEY (hall) REFERENCES public.hall(hall_number) NOT VALID;
 ?   ALTER TABLE ONLY public.event DROP CONSTRAINT event_hall_fkey;
       public          postgres    false    214    203    2790                       2606    32983    excursion excursion_guide_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.excursion
    ADD CONSTRAINT excursion_guide_fkey FOREIGN KEY (guide) REFERENCES public.employee(id) NOT VALID;
 H   ALTER TABLE ONLY public.excursion DROP CONSTRAINT excursion_guide_fkey;
       public          postgres    false    207    206    2796                       2606    32988    excursion excursion_hall_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.excursion
    ADD CONSTRAINT excursion_hall_fkey FOREIGN KEY (hall) REFERENCES public.hall(hall_number) NOT VALID;
 G   ALTER TABLE ONLY public.excursion DROP CONSTRAINT excursion_hall_fkey;
       public          postgres    false    203    207    2790                       2606    65766 %   excursion excursion_master_class_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.excursion
    ADD CONSTRAINT excursion_master_class_fkey FOREIGN KEY (master_class) REFERENCES public.master_class(id) NOT VALID;
 O   ALTER TABLE ONLY public.excursion DROP CONSTRAINT excursion_master_class_fkey;
       public          postgres    false    2822    207    219                       2606    33058    financing financing_fund_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.financing
    ADD CONSTRAINT financing_fund_fkey FOREIGN KEY (fund) REFERENCES public.fund(id) NOT VALID;
 G   ALTER TABLE ONLY public.financing DROP CONSTRAINT financing_fund_fkey;
       public          postgres    false    215    2816    216                       2606    65672 0   master_class master_class_creation_place_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.master_class
    ADD CONSTRAINT master_class_creation_place_id_fkey FOREIGN KEY (creation_place_id) REFERENCES public.creation_place(creation_place_number);
 Z   ALTER TABLE ONLY public.master_class DROP CONSTRAINT master_class_creation_place_id_fkey;
       public          postgres    false    213    219    2810                        2606    65800 1   exhibit_location picture_location_exhibit_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.exhibit_location
    ADD CONSTRAINT picture_location_exhibit_id_fkey FOREIGN KEY (exhibit_id) REFERENCES public.exhibit(id) NOT VALID;
 [   ALTER TABLE ONLY public.exhibit_location DROP CONSTRAINT picture_location_exhibit_id_fkey;
       public          postgres    false    202    220    2788                       2606    65723 2   exhibit_location picture_location_location_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.exhibit_location
    ADD CONSTRAINT picture_location_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.hall(hall_number);
 \   ALTER TABLE ONLY public.exhibit_location DROP CONSTRAINT picture_location_location_id_fkey;
       public          postgres    false    203    220    2790                       2606    65728 3   exhibit_location picture_location_location_id_fkey1    FK CONSTRAINT     �   ALTER TABLE ONLY public.exhibit_location
    ADD CONSTRAINT picture_location_location_id_fkey1 FOREIGN KEY (location_id) REFERENCES public.storage(storage_number);
 ]   ALTER TABLE ONLY public.exhibit_location DROP CONSTRAINT picture_location_location_id_fkey1;
       public          postgres    false    220    205    2794                       2606    65733 3   exhibit_location picture_location_location_id_fkey2    FK CONSTRAINT     �   ALTER TABLE ONLY public.exhibit_location
    ADD CONSTRAINT picture_location_location_id_fkey2 FOREIGN KEY (location_id) REFERENCES public.workshop(workshop_number);
 ]   ALTER TABLE ONLY public.exhibit_location DROP CONSTRAINT picture_location_location_id_fkey2;
       public          postgres    false    2792    204    220                       2606    33018 5   exhibit_purchase purchase_of_exhibits_exhibit_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.exhibit_purchase
    ADD CONSTRAINT purchase_of_exhibits_exhibit_id_fkey FOREIGN KEY (exhibit_id) REFERENCES public.exhibit(id) NOT VALID;
 _   ALTER TABLE ONLY public.exhibit_purchase DROP CONSTRAINT purchase_of_exhibits_exhibit_id_fkey;
       public          postgres    false    202    209    2788                       2606    33028 /   exhibit_purchase purchase_of_exhibits_fund_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.exhibit_purchase
    ADD CONSTRAINT purchase_of_exhibits_fund_fkey FOREIGN KEY (fund) REFERENCES public.fund(id) NOT VALID;
 Y   ALTER TABLE ONLY public.exhibit_purchase DROP CONSTRAINT purchase_of_exhibits_fund_fkey;
       public          postgres    false    2816    216    209                       2606    33063 /   research_activity research_activity_author_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.research_activity
    ADD CONSTRAINT research_activity_author_fkey FOREIGN KEY (author) REFERENCES public.employee(id) NOT VALID;
 Y   ALTER TABLE ONLY public.research_activity DROP CONSTRAINT research_activity_author_fkey;
       public          postgres    false    206    217    2796            "           2606    65818    sale souvenir_sale_fund_fkey    FK CONSTRAINT     w   ALTER TABLE ONLY public.sale
    ADD CONSTRAINT souvenir_sale_fund_fkey FOREIGN KEY (fund) REFERENCES public.fund(id);
 F   ALTER TABLE ONLY public.sale DROP CONSTRAINT souvenir_sale_fund_fkey;
       public          postgres    false    216    2816    221            !           2606    65813 "   sale souvenir_sale_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sale
    ADD CONSTRAINT souvenir_sale_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.shop(id);
 L   ALTER TABLE ONLY public.sale DROP CONSTRAINT souvenir_sale_product_id_fkey;
       public          postgres    false    212    2808    221                       2606    32998    visitor visitor_excursion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.visitor
    ADD CONSTRAINT visitor_excursion_fkey FOREIGN KEY (excursion) REFERENCES public.excursion(id) NOT VALID;
 H   ALTER TABLE ONLY public.visitor DROP CONSTRAINT visitor_excursion_fkey;
       public          postgres    false    208    2798    207            �   �   x�u��qD!C�V) �2��^RM*I#����d��Cf.~I�%��������o��og?:Mò��h��8!��L3�B����N��C��u���.+zM���-RR�l%��4A����>?r�^FP��f�U(�n��tk�B�I
�6����}����4$��N8X�|��5C����L���P�����6=��epv]G����ki��ֈ��&;��      �   T  x�}S�n1];_�=r��c�ac����&�vI�R���hA��!m��4��q�ydE������"��s��_�����_�2�q���o`��+��O�;>/��FcB1�蕶�pØM�^�}�ӳC��o�e�� ����q��k!j�)�LD#-�Vh��ӷ�Y��dP9��f[| ��J���pP�v^��7[���4bS���K4póc�`������,9����y�-�����FL�K�����d�=�Ae ����U`����9��o�*�����&L�`��&���
��2�|��7@yA�s�g_K0�UbF
���h�,�����un�bn�]qx�.���] �P\��.K'�R
Za�������=V�T��x��z	1��9T]�8�-w4��;T	i���a�M8lܱ�[kW�
�۱�C-蠋�7�cJ1ce7��f��A��J����5ZSҿ��]��eL�%���!�LA+)�"(K�f�4q��>bJ�7A���J��9����Bk��M�i��%�� �&�z3W�)#4$e0�%T��������z}��t~c(      �   .   x�3�44༰��.#N# k����&H���F�0v� �AX      �   �  x�u�An�@���)8@if@���P�qcӅm��6ڤIwFQ[�����BO��Z��¼����J�34��j*\z��NiA+�i�Y�L��B%q���S��w�ַ�r��j\Kё����JJ�7�_�3�0h��#m X���B7É���C�H����wޢRg�CtBK9��sH�Q�vi��=Y���O��c�;
a�S��u��W��kĖ.���>dÙ�%K�^҆�J�m2�V�������F߷���>Q���<��<��F���y,�=m�#O&��I���~���g������G�B�.M�oy�С��^�j`����b�5�S������F{���=f͕م�&�!��
���D0��kۧ��m��cC���m��7��Ê+/��`({a���[��[>28��	�|��MEE�Ix���5��Jڶ���`��'_�M���q�?�w>i      �   �   x�m�I
�@D�U����2��äu�ҫ4���7������T�G�Tj�G=�X�&K�<�8������_D&ԓnZ�Z4�q�b����
<ۯ�e�m����
z�_����@\�Þ��On�      �   �   x�EPYn1���"���=Kâ�P���V��1\��F��AH���~�U��3v�?�?z�������*1���c�(:y	�QE���lfs[��#�h�8��@�κs[�)�kw�p�Φ����&���a,�eC∹%^��p�5aV���.�8e'7��CT�������Y���/Ӣ:��8��u"I4s����;�cOR?��:���
\��      �   1  x���AR�@E�3���53����0��nH��.\E�A1��
�W�$�&E��0����n�r��Z܊���E=�kP޺���(v
��W֚߼W�F�>9�J*.y�KC��QN�3D+C/�Z�z�-?QK-�f�+�G�Hp�������up������b�A1hKxZ�E;������[�t}�-@ҳ�넿4HE%J�'H;ht�����jP��:�0T�N"B���}�@d��9��f8��I��O`�#FK�r��z�����^AF�*�0�-�S��ٵ����I      �   �  x��T[nA�N1���>�.��0<l"�8d�#�<��'��r��^��F��Y>!���ݝ����ꉍ��?��������������d�������K��g�ArY[��{|��o��kw�n3�đ�gF;�B\#a�-@���Jr��7���<[��"V��)N�	�Y|�n��[��4�F��q��[��nA��ʳfi��� p�G�qV��o�= 3�_�7�'�)J��m�Q@��*h�J�i�3���[��Pdy�q��M�&��c����ȱ	8VK�$e�!jb9�@s��v�2�(���F��89���w4�EB��Ǫȭ}!�R'M�QV�ĽdZ�v4Ԝ]�s�aY�

�Q�
�T�A�|B��_S�
���f5���L�.�p�Qc�s��|/���dty&O��慩kXi(q�2�b�A=B&Q��AK��7 �{rR�c����
�t�I��zv���jL�%qKr&Yj�24�F]?;��*[5�cq��� ��x�p�� fɡ!��ɤ�<^�8�(�+��BN��Xs�	+V�FLȚXs���� mG�T�-��Z/�s�Qũǥ� t�8�%w��)& M�'K��W����-�.y�:!%�D{�h��	I�Q��X�Jىt��@/2�.����z���-'7�U��h�Y�|�      �   x   x�m��1D�3� l'��B1,�J�Bb)��)R���y��_�|�@��X��{WV*m`�*Ӹ2���K<|��/��	E�e��Bf�f*�3�H�:x�	�����D��UX�~��ۉ���a�      �   T   x�}�A�0��Es���xAJ0�)(A L߻B`�}����9.��tUTt�����ݣ�YEB�6g�V�5Hc_���0(�      �   6  x����N�P��ӧ�^K���vǃ�)J�A�4`d��B%�y�ib�g��}�ĹU	7��Lffq�9���QA�ϵ�ܧ-m��lߧg*쀇%弸�"P(A ~Lq��,`/��:Tq$ABR�h��Z+IO+YǓ@{M/���k�ؙk�x~e���4��8D��ё�4�` ��O�f����F���Wg3ᑦ�g����+vV0��Q��Fi�Lۭ��MΎW����*ʿu�4f�܂�9��A�(��lT��*�,�<�8�f����j�����%4��K��y�=]!�      �   �   x�M���0F��� �?��	&����N�HKA���V{@�X����c��	r���Df�蚋?:�e���ˬ�$�be	ʿ�OLF�����6����;�^R0�
�~U��t���v<�W������1����_��u�      �   =   x�%���0�0L�c�t��?G\��N�.���`a��K}2�`��b����1�l�<$/�<      �   A  x�mQAN�0<�_����7<�mT	���3 ��$�I��1��=ıw�3�����
�q@ҹ.���P���"�����N�����o���}<C�dƂ�
���F*'�L&#�h������Zg�u��h��h���ߚ�BL�'�=���D�l�搫q��^�	�rOy�Zg�zC��L���\�ط�zKl�3�3	�uF��Fop�V���D��x9�✅Q�b�Gz7��3g+D�s��e����lǣ��X.,,��s�3p��S���xK�w:.���J&a*x�Se��쫢�O<�� ����%�p}B����      �   �   x�=PKN1[��"J�IK��a�V�,�(����0�o�
΍pR`����~~v���A�_�*�ѡ��戁��'F�g^	�[��]���a,̼�JG�R��k���يTJ�Ʃ���.�2W3�c�����n���WjLh+-]HΙ���j�=�N9rv$���JsθF�
�]ՍŖ棭<�Xv��ږ��k�B���X��]	�.4�P*p��ߙ�d�QqdJ��6c�\)�~ �5ɷ      �   �   x�e��1��

@ȟ8	�l5T��p�R�[B��yҌ'�u
ѝ��y��E~82*�P��2��o���$�P�)�8Ѷ��*�+C-��Y���RCU�j\����m�6�y<Sǀ圗�챍i�7[�Y|e,e^U�r<J)_�^N      �     x��SMKQ]��+Y����&�m���"��ƍ�PB$�1.ܙT��tZj��.'iF'������%��1�C(.�䞏{�O�{{H1M��TU�E�+��ϟ�i������ų���n�����^'<[�D`d�_���;�k��B��+��c�)Ƴ�"���L��@�Rb���l{���)�)�ƶk����R?�ml7Z��mGc��K�����4e��=�����y�ҥ탳��&�2X��װ��"�[�e��7e4a{0��e�EÞ��WM��<�1%�#W�P3�r�/�J��e�ȧ����}eWt�
F?+๬�����ײ�i�i����pwǅa��	��@�jS{�	e�����"l��{�bq��
�ƔM�a ����3dn8�}�n�6��n�<l0����X���v�#��Mp6�/}s��l��4���=a�c�B8�O|�|	|�G���R�08
�$#�AWc�^P��ǅாc9���-j@gs��ȐU��:s/+DfR�\�rP+��{��,���X4-      �   <   x����0�0LeC���t�9J�8	��p���dy=��Ф�h��L�9'�����|�
q      �   5  x�m�]N�@��wO� �'�܅�4�K�B��*A9A�6RHHz��1�4j}��c�Q�@�0C��+4(�J����*d�Ɣ��X�-E"�����QV���w�m�QP&�*<�TY��'�ED-�E���*G�W�dW�c���
m�%�|�P1��N�1=�*k�N^cz/�0�e��|>���b�pr'��>�9VǭN��h'��ϵ��κ���`Nߌ��_�}O�`�E�S�5m4��a[Y�����]\��kȚ�[a5⌅�'�%S�n���y����m�/�W�{a�h�I����Z��Xr�      �   5   x���	 0�f���1���G��!$�@6LԨ���%�y�Z��"� �?     