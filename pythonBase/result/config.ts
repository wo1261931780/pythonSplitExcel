import { Config } from "./src/config";

export const defaultConfig: Config = {
  /** URL to start the crawl, if sitemap is provided then it will be used instead and download all pages in the sitemap
   * 中文意思是：开始爬行的URL，如果提供了站点地图，则将使用站点地图并下载站点地图中的所有页面
   */
  url: "https://ma.sjtu.edu.cn/szdw.htm",
  // url: "https://ma.sjtu.edu.cn/info/1196/7186.htm?id=289",
  /** Pattern to match against for links on a page to subsequently crawl
   * 中文意思是：用于匹配要在页面上链接的模式，以便随后爬行
  */
  // match: "https://www.builder.io/c/docs/**",这里写错了，应该写链接
  match: "https://ma.sjtu.edu.cn/info/1196/**",
  /** Selector to grab the inner text from
   * 中文意思是：选择器以抓取内部文本
  */
  // selector: `body > div.box.nbg > div.nycon > div > div > div.main-right > div.right-nr > div:nth-child(3) > div > a`,// 可以删除
  // selector: `body > div.box.nbg > div.nycon > div > div > div.main-right > div.right-nr > div:nth-child(3) > div.jiao-con`,// 可以删除
  /** Don't crawl more than this many pages
 * 中文意思是：不要爬行超过这么多页
 */
  maxPagesToCrawl: 60,
  /** File name for the finished data
   * 中文意思是：完成数据的文件名
  */
  outputFileName: "output.json",
  /** Optional resources to exclude
  *中文意思是：要排除的可选资源
  * @example
  * ['png','jpg','jpeg','gif','svg','css','js','ico','woff','woff2','ttf','eot','otf','mp4','mp3','webm','ogg','wav','flac','aac','zip','tar','gz','rar','7z','exe','dmg','apk','csv','xls','xlsx','doc','docx','pdf','epub','iso','dmg','bin','ppt','pptx','odt','avi','mkv','xml','json','yml','yaml','rss','atom','swf','txt','dart','webp','bmp','tif','psd','ai','indd','eps','ps','zipx','srt','wasm','m4v','m4a','webp','weba','m4b','opus','ogv','ogm','oga','spx','ogx','flv','3gp','3g2','jxr','wdp','jng','hief','avif','apng','avifs','heif','heic','cur','ico','ani','jp2','jpm','jpx','mj2','wmv','wma','aac','tif','tiff','mpg','mpeg','mov','avi','wmv','flv','swf','mkv','m4v','m4p','m4b','m4r','m4a','mp3','wav','wma','ogg','oga','webm','3gp','3g2','flac','spx','amr','mid','midi','mka','dts','ac3','eac3','weba','m3u','m3u8','ts','wpl','pls','vob','ifo','bup','svcd','drc','dsm','dsv','dsa','dss','vivo','ivf','dvd','fli','flc','flic','flic','mng','asf','m2v','asx','ram','ra','rm','rpm','roq','smi','smil','wmf','wmz','wmd','wvx','wmx','movie','wri','ins','isp','acsm','djvu','fb2','xps','oxps','ps','eps','ai','prn','svg','dwg','dxf','ttf','fnt','fon','otf','cab']
*/
  // resourceExclusions?: string[];
  /** Optional maximum file size in megabytes to include in the output file
   * 中文意思是：可选的最大文件大小（以兆字节为单位），以包含在输出文件中
  */
  // maxFileSize?: number;
  /** Optional maximum number tokens to include in the output file
   * 中文意思是：可选的最大令牌数，以包含在输出文件中
  */
  maxTokens: 2000000
};
