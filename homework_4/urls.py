import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url")
    return parser


urls = [
    "https://sportishka.com/uploads/posts/2022-11/1667498997_20-sportishka-com-p-avtomobil-marusya-instagram-22.jpg",
    "https://sportishka.com/uploads/posts/2022-11/1667483802_12-sportishka-com-p-lada-marusya-krasivo-13.jpg",
    "https://sportishka.com/uploads/posts/2022-11/1667560376_25-sportishka-com-p-chernaya-marusya-mashina-vkontakte-29.jpg",
    "https://www.avtovzglyad.ru/media/article/marussia-b2-coupe-1-generation.jpg.1280x720_q85_box-0%2C108%2C2064%2C1268_crop_detail_upscale.jpg",
    "http://www.autoade.ru/wp-content/uploads/2018/04/autowp.ru_marussia_b1_4.jpeg",
    "http://mtdata.ru/u23/photoCD89/20751536137-0/original.jpg",
    "https://sportishka.com/uploads/posts/2022-11/1667499021_55-sportishka-com-p-avtomobil-marusya-instagram-59.jpg",
    "https://pibig.info/uploads/posts/2022-11/1668530913_5-pibig-info-p-marusya-krasivo-5.jpg",
    "https://drikus.club/uploads/posts/2022-12/1671822918_drikus-club-p-gonochnaya-mashina-marusya-avtomobili-kras-22.jpg",
    "https://w.forfun.com/fetch/cc/ccab4974d9cec7e9e121c95c737525bd.jpeg?w=1600",
]

if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    urls.append(namespace.url)
