export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  rating: number;
  image: string;
  kaspi: string;
  category: string;
  likes: number;
}

export const products = [
  {
    id: 1,
    name: 'Ноутбук Apple MacBook Air 13 MGND3 золотистый',
    price: 498000,
    description:
      'диагональ экрана: 13.3 дюйм, процессор: Apple M1, видеокарта: Apple M1 8 core, размер оперативной памяти: 8 ГБ, тип жесткого диска: SSD, общий объем накопителей: 256 ГБ',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h48/h65/33286638993438/apple-macbook-air-2020-13-3-mgnd3-zolotistyj-100797576-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/apple-macbook-air-13-mgnd3-zolotistyi-100797576/?c=750000000#!/item',
    category: "Ноутбуки",
    likes: 0
  },
  {
    id: 2,
    name: 'Ноутбук Lenovo IdeaPad 3 15ITL6 82H8005GRK серебристый ',
    price: 169990,
    description:
      'диагональ экрана: 15.6 дюйм, процессор: Intel Pentium Gold 7505, размер оперативной памяти: 8 ГБ, тип жесткого диска: SSD, общий объем накопителей: 256 ГБ',
    rating: 4.5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h8f/h3a/66993674190878/lenovo-ideapad-3-15itl6-82h8005grk-serebristyi-108090705-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/lenovo-ideapad-3-15itl6-82h8005grk-serebristyi-108090705/?c=750000000#!/item',
    category: "Ноутбуки",
    likes: 0
  },
  {
    id: 3,
    name: 'Ноутбук Acer Nitro 5 AN515-57 NH.QEKER.004 черный',
    price: 389700,
    description:
      'диагональ экрана: 13.3 дюйм, процессор: Intel Core i5 11400H, видеокарта: NVIDIA GeForce GTX 1650, размер оперативной памяти: 16 ГБ, тип жесткого диска: SSD, общий объем накопителей: 512 ГБ',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h2e/hc4/67236399185950/acer-nitro-5-an515-57-nh-qeker-004-chernyi-108194028-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/acer-nitro-5-an515-57-nh-qeker-004-chernyi-108194028/?c=750000000#!/item',
    category: "Ноутбуки",
    likes: 0
  },
  {
    id: 4,
    name: 'Ноутбук ASUS TUF Gaming A15 FA506IHRB-HN084 90NR07G7-M008C0 черный',
    price: 349930 ,
    description:
      'диагональ экрана: 15.6 дюйм, процессор:AMD Ryzen 5 4600H, видеокарта: nVidia GeForce GTX1650, размер оперативной памяти: 8 ГБ, тип жесткого диска: SSD, общий объем накопителей: 512 ГБ',
    rating: 4.7,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h6b/h33/62100002701342/asus-tuf-gaming-a15-fa506ihrb-hn084-90nr07g7-m008c0-cernyj-106255184-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/asus-tuf-gaming-a15-fa506ihrb-hn084-90nr07g7-m008c0-chernyi-106255184/?c=750000000#!/item',
    category: "Ноутбуки",
    likes: 0
  },
  {
    id: 5,
    name: 'Ноутбук Lenovo IdeaPad 1 14IGL05 81VU00H3RU серый',
    price: 139990,
    description:
      'диагональ экрана: 14 дюйм, процессор:Intel Celeron N4020, видеокарта:Intel UHD Graphics 600, размер оперативной памяти: 4 ГБ, тип жесткого диска: SSD, общий объем накопителей: 128 ГБ',
    rating: 4.5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h5e/he2/67940461740062/lenovo-ideapad-1-14igl05-81vu00h3ru-seryi-108464874-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/lenovo-ideapad-1-14igl05-81vu00h3ru-seryi-108464874/?c=750000000#!/item',
    category: "Ноутбуки",
    likes: 0
  },

  {
    id: 6,
    name: 'Фитнес-браслет Xiaomi Smart Band 7 Pro белый',
    price: 36390,
    description:
      'Цвет корпусаЖ белый, технология экрана: AMOLED, интерфейсы: bluetooth, время работы: до 12 дней',
    rating: 4.4,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h1e/hce/61984745553950/xiaomi-smart-band-7-pro-belyj-106194157-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/xiaomi-smart-band-7-pro-belyi-106194157/?c= 750000000#!/item',
    category: "Часы",
    likes: 0
  },
  {
    id: 7,
    name: 'Часы SKMEI 1251 черный',
    price: 3762,
    description:
      'Цвет черный, тип: кварцевые,способ отображения времени: цифровой (электронный), материал корпуса: пластик, нержавеющая сталь',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h0c/h75/48515102048286/skmei-1251-cernyj-103561408-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/skmei-1251-chernyi-103561408/?c=750000000#!/item',
    category: "Часы",
    likes: 0
  },
  {
    id: 8,
    name: 'Часы CASIO MTP-VD01D-1BVUDF серебристый',
    price: 18290,
    description:
      'тип: кварцевые, способ отображения времени: аналоговый (стрелки), материал корпуса: сталь,противоударные: Нет',
    rating: 4.9,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hac/h39/31760016211998/casio-mtp-vd01d-1bvudf-silver-21401969-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/casio-mtp-vd01d-1bvudf-serebristyi-21401969/?c=750000000#!/item',
    category: "Часы",
    likes: 0
  },
  {
    id: 9,
    name: 'Часы VAIS VV-001 белый, серебристый',
    price: 14900 ,
    description:
      'тип: кварцевые,способ отображения времени: аналоговый (стрелки), материал корпуса: металлический сплав, цвет: белый, ,серебристый',
    rating: 4.4,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h68/hb2/66616008409118/chasy-vv-001-belyi-seryi-serebristyi-molochnyi-107938116-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/vais-vv-001-belyi-serebristyi-107938116/?c=750000000#!/item',
    category: "Часы",
    likes: 0
  },
  {
    id: 10,
    name: 'Часы CASIO MTP-1375L-1AVDF черный',
    price: 24961,
    description:
      'тип: кварцевые,способ отображения времени: аналоговый (стрелки), материал корпуса: сталь,цвет: черный',
    rating: 4,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h0d/h68/31762831540254/casio-mtp-1375l-1avdf-black-21400938-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/casio-mtp-1375l-1avdf-chernyi-21400938/?c=750000000#!/item',
    category: "Часы",
    likes: 0
  },

  {
    id: 11,
    name: 'Наушники Sony WH-1000XM4 черный',
    price: 199866,
    description:
      'тип: гарнитура, вид: накладные, подключение: беспроводное, тип акустического оформления: закрытые, тип крепления: оголовье, система активного шумоподавления: Да, микрофон: Да',
    rating: 4.9,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h4a/h11/32844899811358/sony-wh-1000xm4b-cernyj-100471997-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/sony-wh-1000xm4-chernyi-100471997/?c=750000000#!/item',
    category: "Наушники",
    likes: 0
  },
  {
    id: 12,
    name: 'Наушники Apple AirPods Pro 2nd generation белый',
    price: 120879,
    description:
      'вид: внутриканальные, подключение: беспроводное, тип акустического оформления: закрытые, тип крепления: без крепления, система активного шумоподавления: Да',
    rating: 4.5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hba/hf8/62281477259294/apple-airpods-pro-2nd-generation-belyj-106362968-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/apple-airpods-pro-2nd-generation-belyi-106362968/?c=750000000#!/item',
    category: "Наушники",
    likes: 0
  },
  {
    id: 13,
    name: 'Наушники Realme Buds T100 черный',
    price: 13799,
    description:
      'тип: гарнитура, вид: внутриканальные, подключение: беспроводное, тип акустического оформления: закрытые, система активного шумоподавления: Да',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h6b/hd2/65147416936478/realme-buds-t100-chernyi-107357596-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/realme-buds-t100-chernyi-107357596/?c=750000000#!/item',
    category: "Наушники",
    likes: 0
  },
  {
    id: 14,
    name: 'Наушники TWS F9-5 черные',
    price: 3377,
    description:
      'система активного шумоподавления: Нет,тип акустического оформления: полуоткрытые , подключение: беспроводное, вид: внутриканальные,тип: гарнитура ',
    rating: 4,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/ha2/h0e/47809640824862/tws-f9-5-cernyj-101769530-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/tws-f9-5-chernye-101769530/?c=750000000#!/item',
    category: "Наушники",
    likes: 0
  },
  {
    id: 15,
    name: 'Наушники JBL Tune 510BT черный',
    price: 23945,
    description:
      'подключение: беспроводное, микрофон: Да, система активного шумоподавления: Нет,тип акустического оформления: закрытые ,тип: гарнитура ',
    rating: 4.9,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h3d/h1d/33957524537374/jbl-tune-510bt-cernyj-101420081-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/jbl-tune-510bt-chernyi-101420081/?c=750000000#!/item',
    category: "Наушники",
    likes: 0
  },

  {
    id: 16,
    name: 'Телевизор LG 77C1RLA 196 см белый',
    price: 2999990,
    description:
      'тип: OLED-телевизор, диагональ: 77 дюйм, разрешение: 3840x2160, поддержка HD: 4K UHD, технология Smart TV: Да, wi-Fi: Да, входы: HDMI',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc9/h72/47509676621854/lg-77c1rla-195-sm-belyj-103038965-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/lg-77c1rla-196-sm-belyi-103038965/?c=750000000#!/item',
    category: "Телевизоры",
    likes: 0
  },
  {
    id: 17,
    name: 'Телевизор Yasin LED-32E7000 81 см черный',
    price: 57740,
    description:
      'диагональ: 32 дюйм, разрешение: 1366x768,поддержка HD: 720p HD ,wi-Fi: Да , тип: LED-телевизор',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h25/ha0/48926247878686/yasin-led-32e7000-cernyj-103411518-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/yasin-led-32e7000-81-sm-chernyi-103411518/?c=750000000#!/item',
    category: "Телевизоры",
    likes: 0
  },
  {
    id: 18,
    name: 'Телевизор Samsung UE43T5300AUXCE 109 см черный',
    price: 197940,
    description:
      'тип: LED-телевизор, разрешение: 1920x1080, технология Smart TV: Да, wi-Fi: Да,входы: AV, ,компонентный, ,Ethernet (RJ-45), ,USB ',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hdf/h18/49319748468766/samsung-ue43t5300au-chernyi-100182013-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/samsung-ue43t5300auxce-109-sm-chernyi-100182013/?c=750000000#!/item',
    category: "Телевизоры",
    likes: 0
  },
  {
    id: 19,
    name: 'Телевизор TCL 43P615 109 см черный',
    price: 156959 ,
    description:
      'диагональ: 43 дюйм,wi-Fi: Да , разрешение: 3840x2160,поддержка HD: 4K HDR ,входы: аудио, ,оптический, ,VGA, ,HDMI, ,USB, ,Bluetooth ',
    rating: 4.6,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h25/h83/51301311905822/tcl-43p615-cernyj-102569498-3.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/tcl-43p615-109-sm-chernyi-102569498/?c=750000000#!/item',
    category: "Телевизоры",
    likes: 0
  },
  {
    id: 20,
    name: 'Телевизор Xiaomi MI TV P1 L43M6-6ARG 109 см черный',
    price: 204990,
    description:
      'диагональ: 43 дюйм,разрешение: 3840x2160 , поддержка HD: 4K UHD,wi-Fi: Да , входы: аудио, ,оптический, ,композитный, ,HDMI, ,Ethernet (RJ-45), ,USB, ,антенный',
    rating: 4.8,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h26/h5b/49320428371998/televizor-xiaomi-mi-tv-p1-l43m6-6arg-109-sm-cernyj-102743844-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/xiaomi-mi-tv-p1-l43m6-6arg-109-sm-chernyi-102743844/?c=750000000#!/item',
    category: "Телевизоры",
    likes: 0
  }
];

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
