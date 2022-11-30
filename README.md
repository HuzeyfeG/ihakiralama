# ihakiralama
Django ile İHA Kiralama Projesi

###### Programlama Dili: Python
###### Web Framework: Django
###### Database: Postgresql

### Ön Bilgi: 
##### Uygulama tamamen “Postgresql” üzerinden local’de veri saklaması yapmaktadır. Oluşturulan sistem planlandığı gibi “Heroku” platformu üzerinden yayınlanamamıştır. Bunun sebebi “Heroku”’nun artık ücretsiz bir şekilde “Postgresql” hizmeti vermemesidir. Proje dosyaları içerisinde(“/ihakiralama/settings.py”) “Postgresql” için parametre bilgileri verilmiştir. Local Database’de gerekli ayarlamalar yapılarak uygulama çalıştırılabilir ya da proje dosyaları içinde bulunan “db.sqlite3” dosyası aktif hale getirilerek denenebilir. 

###### Özet: 
	Üyelik sistemi ile kullanıcıların hesap oluşturabilmesine olanak sağlanmıştır. Her kullanıcı uygulama üzerinden İHA kiralayabilir veya ilan oluşturabilmektedir. İlanlarda filtrelemeler yaparak istenilen İHA’ya kullanıcı kolayca ulaşabilir. İHA ilanı vermek isteyen kullanıcılarda, ilan oluşturma sayfasından kolayca istenilen formu doldurarak ilanı verebilir.

###### Üyelik Sistemi:
	-Django’nun bize database için hazır olarak tanımladığı “migration”’larından “users” tablosu kullanılmıştır. Üyelik için için Username, Email ve Password bilgileri alınmaktadır. Alınan veriler Django’nun default olarak hazırladığı “users” tablosunda saklanmaktadır. Bu tablonun verileri kullanıcın giriş işlemi için kullanılmaktadır.
	- Kullanıcın uygulamaya giriş yapmak için girdiği bilgiler(“username”, “password”) Django’nun kendi methodu olan “authentication” ve “login” methodları ile sağlanmaktadır. Her yapılan “login” işleminde sisteme tanınan “sessionid” ile kullanıcın kontrolü sağlanmaktadır.

###### İHA Kiralama Sistemi:
	-Database içerisinde İHA bilgilerini saklayabilmek için custom bir model oluşturulmuştur. Bu model(“id”, “name”, “brand”, “description”, “maxWeight”, “altitude”, “flightTime”, “armed”, “image”, “owner”) ilana çıkartılacak olan İHA’nın bilgilerini oluşturmaktadır. Kullanıcı ilan formunu doldurduktan sonra yapılan kontroller sonrası hata ile karşılaşılmazsa veriler database’e kaydedilmektedir. Kaydedilen veriler arasında “image” sütununda İHA’nın fotoğrafının kaydedileceği adres yer almaktadır. Fotoğraf belirtilen adrese kaydedilmektedir.
	-İlan düzenleme işlemlerini kullanıcı oluşturduğu ilanı seçerek belirleyebilir. İsterse yeni bilgiler ile güncelleyebilir isterse ilanı yayından kaldırabilir.
	-Anasayfada, sol kısımda yer alan filtreler yardımı ile kullanıcı aradığı İHA’yı kolayca bulabilir ve kiralama işlemini yapabilir.
###### APİ:
	-Uygulama üzerindeki bütün form işlemleri “/api/” klasörü altında cevaplanmaktadır. Üyelik, giriş, ilan verme, ilan düzenleme, ilan silme gibi tüm istekleri oluşturulan yapı karşılamaktadır. Temel mimari olarak Django’ya ait olan “rest framework” yapısı kullanılmıştır. 
