import json, datetime

data = json.load(open("tools/merged_aniidex.json", encoding="utf-8"))
data_json = json.dumps(data, ensure_ascii=False)
today = datetime.date(2026,9,15).strftime("%d/%m/%Y")

html = """<!doctype html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Aniimo Guide VN — Cẩm Nang Toàn Diện</title>
<style>
  :root{
    --bg:#0f1115; --card:#171a21; --card2:#1e222b; --border:#2a2f3a;
    --fg:#e8eaf0; --muted:#9aa1af; --accent:#f5a524; --accent2:#f43f5e; --accent3:#38bdf8;
    --good:#22c55e; --warn:#f43f5e;
    color-scheme: dark;
  }
  @media (prefers-color-scheme: light){
    :root{ --bg:#f7f7fb; --card:#ffffff; --card2:#f1f2f6; --border:#e3e5ec; --fg:#14161c; --muted:#5b6472; }
  }
  *{box-sizing:border-box;}
  body{margin:0;background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;padding-bottom:60px;}
  .wrap{max-width:1100px;margin:0 auto;padding:0 16px;}
  header.top{padding:22px 16px 14px;text-align:center;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--bg);z-index:20;}
  header.top h1{margin:0 0 4px;font-size:1.5rem;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent;}
  header.top p{margin:0;color:var(--muted);font-size:.8rem;}
  .warn-banner{background:rgba(244,63,94,.12);border:1px solid var(--warn);color:var(--fg);padding:10px 14px;border-radius:12px;margin:14px auto;max-width:1100px;font-size:.85rem;line-height:1.5;}
  .warn-banner b{color:var(--warn);}
  nav.tabs{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;max-width:1100px;margin:10px auto;padding:0 16px;}
  @media(min-width:700px){nav.tabs{grid-template-columns:repeat(8,1fr);}}
  nav.tabs button{background:var(--card);border:1px solid var(--border);color:var(--fg);padding:8px 4px;border-radius:10px;font-size:.68rem;cursor:pointer;font-weight:600;}
  nav.tabs button.active{background:var(--accent);color:#1a1a1a;border-color:var(--accent);}
  section{display:none;max-width:1100px;margin:0 auto;padding:8px 16px 30px;}
  section.active{display:block;}
  h2{font-size:1.2rem;border-left:4px solid var(--accent);padding-left:10px;margin:22px 0 10px;}
  h2:first-child{margin-top:6px;}
  .card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:14px 16px;margin-bottom:12px;}
  table{width:100%;border-collapse:collapse;font-size:.8rem;}
  th,td{padding:6px 8px;border-bottom:1px solid var(--border);text-align:left;vertical-align:top;}
  th{color:var(--muted);font-weight:600;position:sticky;top:0;background:var(--card);}
  .tbl-wrap{overflow-x:auto;border:1px solid var(--border);border-radius:12px;}
  .pill{display:inline-block;padding:2px 8px;border-radius:999px;font-size:.65rem;font-weight:700;margin-right:4px;}
  .pill.t0{background:#f43f5e;color:#fff;} .pill.t05{background:#fb923c;color:#1a1a1a;}
  .pill.t1{background:#facc15;color:#1a1a1a;} .pill.t2{background:#4ade80;color:#1a1a1a;}
  .pill.t25{background:#38bdf8;color:#1a1a1a;} .pill.t3{background:#94a3b8;color:#1a1a1a;}
  .el-badge{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;margin-right:4px;vertical-align:middle;flex:none;}
  .el-badge svg{width:13px;height:13px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
  .el-badge-mini{display:inline-flex;align-items:center;justify-content:center;width:15px;height:15px;border-radius:50%;margin-right:4px;vertical-align:middle;opacity:.92;flex:none;}
  .el-badge-mini svg{width:9px;height:9px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
  .shape-dps{border-radius:7px 18px 7px 18px;}
  .shape-break{border-radius:5px;clip-path:polygon(28% 0%,72% 0%,100% 28%,100% 72%,72% 100%,28% 100%,0% 72%,0% 28%);}
  .shape-support{border-radius:50% 50% 50% 6px;}
  .shape-heal{border-radius:50%;}
  .shape-regen{border-radius:28%;}
  .shape-tank{clip-path:polygon(25% 0%,75% 0%,100% 50%,75% 100%,25% 100%,0% 50%);}
  .shape-utility{clip-path:polygon(50% 0%,100% 50%,50% 100%,0% 50%);}
  .bst-txt{color:var(--muted);font-size:.72rem;}
  .pill.stage-lumin{background:#a5b4fc;color:#1a1a1a;} .pill.stage-gamma{background:#c084fc;color:#1a1a1a;} .pill.stage-nova{background:#fbbf24;color:#1a1a1a;}
  .filters select{padding:9px 12px;border-radius:10px;border:1px solid var(--border);background:var(--card2);color:var(--fg);font-size:.8rem;}
  .chip.reset{background:var(--card2);font-weight:700;}
  .chip .chip-dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:middle;}
  .stat-line{display:flex;flex-wrap:wrap;gap:2px 10px;font-size:.68rem;color:var(--muted);margin-top:6px;border-top:1px dashed var(--border);padding-top:6px;font-variant-numeric:tabular-nums;}
  .stat-line b{color:var(--fg);font-weight:600;}
  .filters{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0;}
  .filters input[type=text]{flex:1 1 200px;padding:9px 12px;border-radius:10px;border:1px solid var(--border);background:var(--card2);color:var(--fg);font-size:.85rem;}
  .chip{padding:6px 10px;border-radius:999px;border:1px solid var(--border);background:var(--card2);color:var(--fg);font-size:.72rem;cursor:pointer;}
  .chip.active{background:var(--accent);color:#1a1a1a;border-color:var(--accent);}
  .grid{display:grid;grid-template-columns:1fr;gap:10px;}
  @media(min-width:640px){.grid{grid-template-columns:1fr 1fr;}}
  @media(min-width:960px){.grid{grid-template-columns:1fr 1fr 1fr;}}
  .mon{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:12px 14px;}
  .mon h4{margin:0 0 4px;font-size:.95rem;}
  .mon .meta{color:var(--muted);font-size:.72rem;margin-bottom:6px;}
  .mon .desc{font-size:.78rem;line-height:1.4;color:var(--fg);opacity:.9;}
  .mon .loc{font-size:.7rem;color:var(--muted);margin-top:6px;border-top:1px dashed var(--border);padding-top:6px;}
  footer{max-width:1100px;margin:30px auto 0;padding:16px;border-top:1px solid var(--border);color:var(--muted);font-size:.72rem;line-height:1.6;}
  code{background:var(--card2);padding:1px 5px;border-radius:5px;}
  .src{font-size:.65rem;color:var(--accent3);font-weight:700;text-transform:uppercase;letter-spacing:.03em;}
  ul{padding-left:20px;} li{margin-bottom:4px;font-size:.85rem;}
  .count{color:var(--muted);font-size:.75rem;margin-bottom:8px;}
</style>
</head>
<body>

<header class="top">
  <h1>🎮 Aniimo Guide VN</h1>
  <p>Cẩm nang cộng đồng — cập nhật lần cuối: __TODAY__ · game ra mắt 16/09/2026</p>
</header>

<div class="wrap">
<div class="warn-banner">
  ⚠️ <b>Lưu ý quan trọng:</b> Hệ thống <b>Rune</b> và <b>Gacha</b> đã bị nhà phát triển Pawprint Studio <b>gỡ bỏ hoàn toàn</b> trước ngày ra mắt (thông báo 03/09/2026). Một số nội dung cũ nhắc tới "Rune Crafting" chỉ còn giá trị lịch sử. Trang này tổng hợp từ nhiều nguồn cộng đồng + wiki chính thức — có thể còn sai lệch nhỏ, sẽ cập nhật liên tục sau khi game ra mắt.
</div>
</div>

<nav class="tabs" id="tabs">
  <button data-tab="tong-quan" class="active">Tổng Quan</button>
  <button data-tab="aniidex">Aniidex</button>
  <button data-tab="doi-hinh">Đội Hình &amp; Gợi Ý</button>
  <button data-tab="vat-pham">Vật Phẩm</button>
  <button data-tab="nguoi-moi">Người Mới</button>
  <button data-tab="roadmap">Roadmap &amp; PvP</button>
  <button data-tab="su-kien">Sự Kiện</button>
</nav>

<section id="tong-quan" class="active">
  <h2>Thông tin phát hành</h2>
  <div class="card">
    <ul>
      <li><b>Thể loại:</b> ARPG hành động thời gian thực, thu phục sinh vật thế giới mở, F2P, <b>không Gacha nhân vật</b>.</li>
      <li><b>Nhà phát triển:</b> Pawprint Studio / Pawprint Interactive Entertainment (hợp tác FunPlus).</li>
      <li><b>Ngày ra mắt:</b> PC/PS5/Xbox: <b>16/09/2026, 10:00 UTC+8</b>. Mobile (iOS/Android): 23/09/2026.</li>
      <li><b>Nền tảng:</b> Steam, Epic Games Store, Microsoft Store, PS5, Xbox Series X|S, iOS, Android — Cross-play + Cross-progression đầy đủ.</li>
      <li><b>Server VN nên chọn:</b> Aniimo-Apac (ping thấp nhất).</li>
      <li><b>Bối cảnh:</b> Lục địa Idyll (hành tinh Astra). Người chơi là Observer thuộc Học viện Polaris, thuần hóa Aniimo và ngăn thế lực hắc ám.</li>
    </ul>
  </div>

  <h2>Cấu hình PC</h2>
  <div class="tbl-wrap"><table>
    <tr><th></th><th>Tối thiểu</th><th>Khuyến nghị</th></tr>
    <tr><td>CPU</td><td>i7-9700 / Ryzen 5 3600X</td><td>i7-12700F / Ryzen 7 7700X</td></tr>
    <tr><td>RAM</td><td>12 GB</td><td>16 GB</td></tr>
    <tr><td>GPU</td><td>GTX 1060 / RX 6600</td><td>RTX 3070 8GB / RX 6800</td></tr>
    <tr><td>Ổ cứng</td><td>45 GB SSD</td><td>45 GB SSD</td></tr>
  </table></div>

  <h2>Hai cơ chế lõi</h2>
  <div class="card">
    <p><b>Command Mode</b> — Aniimo tự động chiến đấu cạnh người chơi, bạn đứng ngoài hỗ trợ/đặt bẫy.<br>
    <b>Twining Mode ("Be One, Be All")</b> — hóa thân trực tiếp thành Aniimo, có <b>I-frame 0.4s</b> khi né, dùng Trait di chuyển đặc hữu (Tunneling / Gliding / Surfing).</p>
    <p><b>Break System:</b> đánh gãy thanh Break (giáp) của mục tiêu → choáng cứng 2.5–3s + nhận thêm 30% sát thương. Chỉ nên ném Aniipod khi máu &lt;20% <i>và</i> Break đã gãy.</p>
  </div>

  <h2>Cross-progression</h2>
  <div class="card">
    <p>Liên kết tài khoản chỉ thực hiện <b>1 lần duy nhất</b> ở lần mở game đầu tiên trên console — nhập đúng email tài khoản cũ vào popup liên kết. Bỏ qua bước này sẽ tạo tài khoản mới <b>vĩnh viễn không thể</b> liên kết lại. Không hỗ trợ cross-server.</p>
  </div>
</section>

<section id="aniidex">
  <h2>Bách khoa Aniimo (Aniidex)</h2>
  <div class="card" style="font-size:.78rem;line-height:1.6;">
    <b>Lưu ý:</b> trang này <u>không xếp Tier List</u> (S/A/B hay T0-T3) vì độ mạnh yếu phụ thuộc rất nhiều vào meta hiện tại, đội hình PvE hay PvP, và trình độ người chơi — dễ gây hiểu lầm nếu lấy 1 bảng cố định. Thay vào đó, mỗi Aniimo hiển thị <b>BST (tổng chỉ số gốc)</b> để tham khảo khách quan, và có gợi ý đội hình cụ thể theo mục đích (Tân thủ / PvE / PvP) ở tab <b>Đội Hình &amp; Gợi Ý</b>.
    <br><b>Biểu tượng hệ:</b> màu + icon = Hệ nguyên tố (hệ phụ hiển thị chấm nhỏ bên cạnh, nếu có). <b>Hình khối huy hiệu:</b> nhọn=DPS, bát giác=Break, bo lệch=Support, tròn=Heal, vuông bo=Regen, lục giác=Tank, thoi=Utility.
    <br><b>Giai đoạn</b> (<span class="pill stage-lumin">Lumin</span> <span class="pill stage-gamma">Gamma</span> <span class="pill stage-nova">Nova</span>): <u>ước tính</u> theo ngưỡng BST (chưa có dữ liệu chuỗi tiến hóa chính thức đầy đủ) — chỉ hiển thị cho 97 Aniimo có nguồn chính thức, không áp dụng cho các mục đánh dấu "fan guide VN". 6 chỉ số chi tiết (HP/ATK/M.DEF/P.DEF/BRK/REGEN) lấy từ wiki.koiseki.com/aniimo, cùng nguồn cho 97 mục này.
  </div>
  <div class="filters">
    <input type="text" id="search" placeholder="Tìm tên Aniimo...">
    <select id="sortSel">
      <option value="num-asc">Sắp xếp: # tăng dần</option>
      <option value="num-desc"># giảm dần</option>
      <option value="bst-desc">BST cao → thấp</option>
      <option value="bst-asc">BST thấp → cao</option>
      <option value="name-asc">Tên A-Z</option>
    </select>
    <span class="chip reset" id="resetBtn">↺ Đặt lại bộ lọc</span>
  </div>
  <div class="filters" id="elemFilters"></div>
  <div class="filters" id="roleFilters"></div>
  <div class="filters" id="stageFilters"></div>
  <div class="count" id="resultCount"></div>
  <div class="grid" id="dexGrid"></div>
</section>

<section id="doi-hinh">
  <h2>🧭 Gợi ý theo mục đích (không phải Tier List cố định)</h2>
  <div class="card">
    <p><b>Tân thủ (0-2 tuần đầu):</b> ưu tiên bắt đủ loài mới trên đường đi hơn là săn "hàng hiếm" — xem chi tiết ở tab Người Mới. Đội hình dễ dùng: 1 DPS chủ lực (Hyper-Carry) + 1 Healer (VD: Gracewing) + 1-2 quái hỗ trợ hệ tương khắc vùng đang đi.</p>
    <p><b>PvE leo tầng / Boss:</b> ưu tiên đội có đủ 3 vai trò DPS/Break/Heal, chọn theo hệ khắc chế mục tiêu (bảng khắc chế bên dưới) hơn là chọn theo "tier mạnh sẵn".</p>
    <p><b>PvP:</b> tham khảo tổ hợp Holy Trinity (Sát thủ + Cleanse + Breaker/CC) bên dưới — nhưng mạnh yếu thực tế đổi liên tục theo bản cập nhật, nên coi đây là gợi ý khởi điểm, không phải bảng xếp hạng cố định.</p>
  </div>

  <h2>Bảng khắc chế nguyên tố</h2>
  <div class="tbl-wrap"><table>
    <tr><th>Hệ</th><th>Khắc</th><th>Bị khắc</th></tr>
    <tr><td>Lửa</td><td>Cỏ, Băng</td><td>Nước, Tối</td></tr>
    <tr><td>Nước</td><td>Lửa, Đất</td><td>Cỏ, Điện, Băng</td></tr>
    <tr><td>Cỏ</td><td>Nước, Đất</td><td>Lửa, Gió, Tối</td></tr>
    <tr><td>Điện</td><td>Nước, Gió</td><td>Đất, Băng</td></tr>
    <tr><td>Đất</td><td>Điện, Băng</td><td>Nước, Cỏ</td></tr>
    <tr><td>Gió</td><td>Cỏ, Tối</td><td>Điện, Sáng</td></tr>
    <tr><td>Tối</td><td>Lửa, Cỏ, Sáng</td><td>Gió, Sáng</td></tr>
    <tr><td>Băng</td><td>Nước, Điện</td><td>Lửa, Đất</td></tr>
    <tr><td>Ánh Sáng</td><td>Gió, Tối</td><td>Tối</td></tr>
  </table></div>
  <p style="font-size:.8rem;color:var(--muted)">Hệ khắc chế: x1.6 sát thương · Hệ bị khắc: x0.625 · Trung lập: x1</p>

  <h2>Đội hình PvP Meta (Holy Trinity)</h2>
  <div class="card"><p><b>Sát thủ:</b> Stellarys / Thornblade &nbsp;·&nbsp; <b>Cleanse bắt buộc:</b> Gracewing &nbsp;·&nbsp; <b>Breaker/CC:</b> Glancer / Fulmintis</p></div>

  <h2>Đội hình PvE nổi bật</h2>
  <div class="card">
    <p><b>Electric Premium:</b> Blazen → Fulmintis → Luminelle → Turbo</p>
    <p><b>Dark One-Shot (Boss Killer):</b> Dreaple + Fragrancier → Inferlupa → Pawney</p>
    <p><b>Full Lightning Burst:</b> Fenmane → Luminelle → Dazmand → Glacy</p>
    <p><b>Grass Crit Sanctuary:</b> Gracewing → Thornblade → Melloblum → Tuckin</p>
  </div>
</section>

<section id="vat-pham">
  <h2>⚠️ Rune & Gacha đã bị gỡ bỏ</h2>
  <div class="card" style="border-color:var(--warn)">
    <p>Theo thư thông báo 03/09/2026: gỡ bỏ Gacha bắt Aniimo Huyền thoại (thay bằng thu thập Legendary Token → tự chế Legendary Aniipod) và gỡ bỏ <b>toàn bộ hệ thống Rune</b>. Hệ thống thay thế (nếu có, có thể là "Capability Awakening") <b>chưa được xác nhận chính thức</b>.</p>
  </div>

  <h2>Aniipod (11 loại)</h2>
  <div class="card"><p>Aniipod, for Teaching, Hyper, Mega, Pro, Trace (auto-lock), <b>Ultra</b> (mạnh nhất thường), Legendary Aniipod, Nicole's, <b>Sparkling Cube</b> (đảm bảo Perfect Potential), Tumbler (bắt cả đàn).</p></div>

  <h2>Trứng (111 quả, 4 bậc)</h2>
  <div class="card"><p>Prismatic (36) · Legendary (43) · Epic (26) · Rare (6). Gồm Zone Egg, Species/Elite Egg, Prismana Egg, Sparkling Egg, Perfect Egg (theo loài hoặc theo vai trò).</p></div>

  <h2>Hệ thống Form đặc biệt</h2>
  <div class="tbl-wrap"><table>
    <tr><th>Form</th><th>Định nghĩa</th><th>Số lượng</th></tr>
    <tr><td>Regional</td><td>Tiến hóa tại đúng vùng địa lý</td><td>78 (Highland 49, Mountain Woods 27, Mudflat 2)</td></tr>
    <tr><td>Weather</td><td>Tiến hóa đúng thời tiết/thời điểm</td><td>19</td></tr>
    <tr><td>Prismana</td><td>Hiếm cầu vồng, chỉ khác ngoại hình</td><td>20</td></tr>
    <tr><td>Umbrabow</td><td>Đối trọng bóng tối của Prismana</td><td>12</td></tr>
    <tr><td>Sparkling</td><td>Lớp "shiny" cộng dồn lên form khác</td><td>69</td></tr>
    <tr><td>Alpha</td><td>Boss khổng lồ ngoài thế giới mở</td><td>19 điểm (Breezy Plains)</td></tr>
    <tr><td>Omega</td><td>Boss khổng lồ loại 2, cơ chế khác Alpha</td><td>4 điểm</td></tr>
  </table></div>
  <div class="card"><p>💡 Mẹo: dùng <b>Sparkling Cube</b> lên Prismana miễn phí (từ Prismana Promise) → có ngay bản vừa Prismana vừa Sparkling, không cần roll.</p></div>
</section>

<section id="nguoi-moi">
  <h2>So sánh 2 Starter</h2>
  <div class="tbl-wrap"><table>
    <tr><th></th><th>Lunara (Moon Fox)</th><th>Helion (Sun Lion)</th></tr>
    <tr><td>Hệ/Vai trò</td><td>Ánh Sáng · DPS tầm xa</td><td>Ánh Sáng · DPS cận chiến</td></tr>
    <tr><td>Chỉ số</td><td colspan="2">Giống hệt nhau: HP 90 / ATK 116 / P.DEF 65 / M.DEF 65 / BREAK 85 / REGEN 83 (BST 504)</td></tr>
    <tr><td>Ưu</td><td>An toàn, đứng xa, giảm kháng địch, tự sustain</td><td>Dồn dập, gom địch, burst mạnh</td></tr>
    <tr><td>Nhược</td><td>Cần setup, ít burst</td><td>Cận chiến cần né đòn chuẩn</td></tr>
  </table></div>
  <p style="font-size:.8rem;color:var(--muted)">Quyết định gần như vĩnh viễn — hiện chưa có cách nào khác để có 2 Starter này.</p>

  <h2>10 việc nên làm đầu tiên</h2>
  <div class="card"><ul>
    <li>Đẩy Wayfarer Level qua cốt truyện chính (mở Talent, tăng trần cấp Aniimo)</li>
    <li>Bắt mọi loài mới trên đường đi thay vì cày trùng loài</li>
    <li>Gom đủ 30 Lumin Amber (nửa phí mở Nurture)</li>
    <li>Mở khóa Nurture, dùng miễn phí mỗi ngày 04:00</li>
    <li>Tiêu Prime Energy trước khi chạm trần 300 (hồi 1đ/6 phút)</li>
    <li>Mở Homeland ngay khi đạt Wayfarer Lv20</li>
    <li>Nâng RV lên cấp 2 sớm (bắt đầu tự động hóa nhân công)</li>
    <li>Đẩy Holo Battle theo sức mạnh đội hình</li>
    <li>Nhận hết phần thưởng reset hàng ngày trước khi thoát game</li>
    <li>Giữ dành Sparkling Cube / Aniipod Ultra / Perfect Egg cho Aniimo thực sự đáng giá</li>
  </ul></div>

  <h2>6 Prismana miễn phí (chọn lúc Junior Wayfarer)</h2>
  <div class="tbl-wrap"><table>
    <tr><th>Prismana</th><th>Hệ/Vai trò</th><th>Điểm mạnh</th></tr>
    <tr><td>Witchin</td><td>Tối · Healer</td><td>BST cao nhất (530), healer duy nhất trong 6 lựa chọn</td></tr>
    <tr><td>Grizbo</td><td>Đất · DPS</td><td>Đòn đánh mạnh nhất nhóm (Rock Smash 227)</td></tr>
    <tr><td>Pawney</td><td>Tối · DPS</td><td>ATK cao nhất nhóm (128)</td></tr>
    <tr><td>Thornblade</td><td>Cỏ · DPS</td><td>Sword Dance cộng dồn, thưởng lối chơi kiên trì</td></tr>
    <tr><td>Turbo</td><td>Gió · Support</td><td>Skill miễn phí mỗi 25s, 5 biến thể form</td></tr>
    <tr><td>Scorchhowl</td><td>Lửa · DPS</td><td>6 biến thể form, bỏng cộng dồn</td></tr>
  </table></div>

  <h2>Homeland — 13 công việc &amp; bậc RV</h2>
  <div class="card">
    <p>9 job hệ nguyên tố + 4 job chung (Carry, Artisanship, Leisure, Perfumery). Nguyên tắc: phủ đủ job cần trước, rồi mới nâng job yếu nhất.</p>
    <p><b>Đội khởi đầu tốt (RV2, 8 slot):</b> Turbo, Shrubclaw, Fragrancier, Thornblade, Stellarys, Glacy, Emberpup (tạm), Pranky (tạm).</p>
  </div>
</section>

<section id="roadmap">
  <h2>Roadmap 30 ngày</h2>
  <div class="card">
    <p><b>Tuần 1 (1-7):</b> Tutorial, chọn Starter, bắt Emberpup, mở 6 tháp dịch chuyển, đặt móng Homeland, bắt Gracewing, lên Lv25.</p>
    <p><b>Tuần 2 (8-14):</b> Mở vùng Băng/Lửa, Co-op săn Boss, bắt Thornblade &amp; Coraliz, thử 3v3 Egg Heist, chế Aniipod Ultra.</p>
    <p><b>Tuần 3 (15-21):</b> Lên Lv40, kích hoạt Prismana Promise, tiến hóa tối thượng đội hình, hoàn thành Mobile Base.</p>
    <p><b>Tuần 4 (22-30):</b> Săn Alpha Stellarys, dùng Inheritance chuyển tài nguyên, leo Top PvP &amp; Diamond Egg Heist.</p>
  </div>

  <h2>Cày cấp thần tốc 3 ngày đầu</h2>
  <div class="card"><ul>
    <li><b>Hyper-Carry:</b> dồn 85% EXP Gems vào 1 DPS chủ lực lên Lv30-35 ngay ngày 1-2</li>
    <li>Bắt loài mới lần đầu = x3-x5 EXP (dùng bẫy Tumbler gom cả đàn)</li>
    <li>Bám Training Program, đẩy Holo-Battle Sim tầng 15-20 (không tốn Stamina)</li>
    <li>Săn 4 Alpha Boss cấp thấp: Roobeak (Lv12), Aquapup (Lv18), Thornblade (Lv25), Grizbo (Lv32)</li>
    <li>Không để Stamina chạm trần 180 (hồi 1đ/6 phút)</li>
  </ul></div>

  <h2>3 kỹ thuật PvP sống còn</h2>
  <div class="card"><ol>
    <li><b>I-frame nuốt chiêu cuối:</b> bấm Twining/Dash đúng lúc để dùng 0.4s bất tử</li>
    <li><b>Đếm Cooldown Dash địch</b> (4-5s) rồi tung khống chế ngay khi chúng vừa lướt xong</li>
    <li><b>Animation Canceling:</b> bấm skill Command Mode → Twine ngay → đòn thường bồi liền</li>
  </ol></div>

  <h2>5 sai lầm cần tránh</h2>
  <div class="card"><ol>
    <li>Nâng sao bừa bãi quái Common</li>
    <li>Bỏ quên Healer (Gracewing) — không qua nổi ải 35+</li>
    <li>Bỏ bê Homeland — thiếu bóng ném &amp; thuốc hồi ở Endgame</li>
    <li>Chọn Prismana theo màu sắc thay vì bổ trợ hệ</li>
    <li>Đứng yên bấm chiêu trong PvP — phải di chuyển liên tục</li>
  </ol></div>
</section>

<section id="su-kien">
  <h2>Lịch sự kiện 6 tuần đầu</h2>
  <div class="card">
    <p><b>Tuần 1-2 (16-29/09):</b> Mở cụm Apac, x2 EXP tân thủ, 23/09 mở Mobile.</p>
    <p><b>Tuần 3-4 (30/09-14/10):</b> Season 1 Egg Heist, x2 tỉ lệ Sparkling cuối tuần, mở Sanctum Puzzles.</p>
    <p><b>Tuần 5-6 (15-28/10):</b> Prismana Flow cực hạn, mở chuỗi tiến hóa Inferlupa.</p>
    <p><b>Sự kiện dài:</b> Tracing the Trail (20/09–09/12), Legendary Journey: Irisalis (25/09–09/12).</p>
    <p><b>Vein Abundance (tăng tỉ lệ Prismana):</b> 18-20/09 Forest of Falling Stars → 21-27/09 Glynsera → 28/09-04/10 Melloblum → 05-11/10 Waleetle → 12-18/10 Inferlupa → 19-25/10 Carnival (cả 4).</p>
  </div>

  <h2>Quà Pre-Registration (30 triệu đăng ký)</h2>
  <div class="card"><p>5M: 5x Aniipod T1 + 5.000 Vàng · 15M: 10x Experience Gems · 25M: 3x Prismana Shard + danh hiệu · 30M: Trang phục Sunlit Meadow Outfit vĩnh viễn.</p></div>

  <h2>Mã Redeem</h2>
  <div class="card"><p>Tính đến 15/09/2026: <b>chưa có mã nào</b> được công bố chính thức. Cẩn thận với các trang liệt kê "mã đang hoạt động" — đều là bịa đặt cho tới khi Pawprint Studio công bố qua kênh chính thức.</p></div>
</section>

<footer>
  <p><b>Nguồn tổng hợp:</b> gói tài liệu cá nhân (video ZakkuVerse + aniimotools.dev), wiki cộng đồng aniimoguide.com, và wiki chính thức wiki.aniimo.com (Pawprint Interactive Entertainment). Trang này do người hâm mộ tự làm, không thuộc Pawprint Studio.</p>
  <p>Cập nhật lần cuối: __TODAY__. Dữ liệu trước ngày ra mắt có thể thay đổi khi game chính thức phát hành 16/09/2026 — sẽ cập nhật liên tục sau đó.</p>
</footer>

<script>
const DATA = __DATA__;

let activeElem = "all";
let activeRole = "all";
let activeStage = "all";

const ELEMENT_ORDER = ["Lửa","Điện","Ánh Sáng","Thảo Mộc","Gió","Nước","Băng","Bóng Tối","Đất"];
const ROLE_ORDER = ["DPS","Break","Support","Heal","Regen","Tank","Utility"];
const STAGE_ORDER = ["Lumin","Gamma","Nova"];
function normElem(tok){
  if(tok==="Cỏ") return "Thảo Mộc";
  if(tok==="Tối") return "Bóng Tối";
  return tok;
}
function elemParts(elemStr){
  return (elemStr||"").split("/").map(s=>normElem(s.trim())).filter(Boolean);
}
function elemMatches(d, filterElem){
  return elemParts(d.elem).includes(filterElem);
}

const ELEMENT_MAP = {
  "Lửa":{c:"#e03131",icon:"fire"},
  "Điện":{c:"#f08c00",icon:"electric"},
  "Ánh Sáng":{c:"#fcc419",icon:"holy"},
  "Thảo Mộc":{c:"#66a80f",icon:"grass"},
  "Cỏ":{c:"#66a80f",icon:"grass"},
  "Gió":{c:"#2f9e44",icon:"wind"},
  "Nước":{c:"#1971c2",icon:"water"},
  "Băng":{c:"#15aabf",icon:"ice"},
  "Bóng Tối":{c:"#7048e8",icon:"dark"},
  "Tối":{c:"#7048e8",icon:"dark"},
  "Đất":{c:"#a67c52",icon:"rock"}
};
const ROLE_SHAPE_CLASS = {DPS:"shape-dps",Break:"shape-break",Support:"shape-support",Heal:"shape-heal",Regen:"shape-regen",Tank:"shape-tank",Utility:"shape-utility"};
function badgeSvg(key){
  const P = {
    fire:'<path d="M12 2c-1.2 4-5 5.2-5 10a5 5 0 0010 0c0-1.8-.8-3-1.8-4 .1 2-.9 3.2-1.9 2.4 1.1-2 0-5.4-1.3-8.4z"/>',
    electric:'<path d="M13 2 3 14h7l-1 8 11-14h-7z"/>',
    holy:'<path d="M12 2l1.8 6.6L20 10l-6.2 1.6L12 18l-1.8-6.4L4 10l6.2-1.4z"/>',
    grass:'<path d="M4 20c9 0 15-6 15-15 0 0-13-1-15 8-1.5 4.5.5 7 0 7z"/>',
    wind:'<path d="M3 7h11a3 3 0 100-3"/><path d="M3 12h16a3 3 0 110 3"/><path d="M3 17h9a3 3 0 100 3"/>',
    water:'<path d="M12 3c4.5 5 7 8.6 7 12a7 7 0 01-14 0c0-3.4 2.5-7 7-12z"/>',
    ice:'<path d="M12 2v20M4.5 6.5l15 11M19.5 6.5l-15 11"/>',
    dark:'<path d="M15.5 3a9 9 0 100 18 7.2 7.2 0 010-18z"/>',
    rock:'<path d="M3 20l5.5-10 3.5 5.5 2.5-4.5L21 20z"/>'
  };
  return '<svg viewBox="0 0 24 24">' + (P[key]||P.rock) + '</svg>';
}
function elBadgeHTML(elemStr, role){
  if(!elemStr) return '';
  const parts = elemStr.split("/").map(s=>s.trim());
  const shapeClass = ROLE_SHAPE_CLASS[role] || "shape-support";
  const primary = ELEMENT_MAP[parts[0]] || {c:"#868e96",icon:"rock"};
  let out = `<span class="el-badge ${shapeClass}" style="background:${primary.c}" title="${elemStr} · ${role||""}">${badgeSvg(primary.icon)}</span>`;
  if(parts[1]){
    const sec = ELEMENT_MAP[parts[1]] || {c:"#868e96",icon:"rock"};
    out += `<span class="el-badge-mini" style="background:${sec.c}" title="${parts[1]}">${badgeSvg(sec.icon)}</span>`;
  }
  return out;
}

function uniq(arr){ return [...new Set(arr)]; }

function makeChipRow(boxId, allLabel, options, stateGetSet, extraCls){
  const box = document.getElementById(boxId);
  box.innerHTML = `<span class="chip active" data-v="all">${allLabel}</span>` +
    options.map(([v,label,dot])=>`<span class="chip" data-v="${v}">${dot? `<span class="chip-dot" style="background:${dot}"></span>`:""}${label}</span>`).join("");
  box.querySelectorAll(".chip").forEach(c=>c.addEventListener("click",()=>{
    stateGetSet(c.dataset.v);
    box.querySelectorAll(".chip").forEach(x=>x.classList.remove("active"));
    c.classList.add("active");
    render();
  }));
}

function renderFilters(){
  makeChipRow("elemFilters", "Tất cả hệ", ELEMENT_ORDER.map(e=>[e,e,(ELEMENT_MAP[e]||{}).c]), v=>activeElem=v);
  makeChipRow("roleFilters", "Tất cả vai trò", ROLE_ORDER.map(r=>[r,r]), v=>activeRole=v);
  makeChipRow("stageFilters", "Tất cả giai đoạn", STAGE_ORDER.map(s=>[s,s]), v=>activeStage=v);

  document.getElementById("resetBtn").addEventListener("click", ()=>{
    activeElem = activeRole = activeStage = "all";
    document.getElementById("search").value = "";
    document.getElementById("sortSel").value = "num-asc";
    document.querySelectorAll(".filters .chip[data-v]").forEach(c=>{
      c.classList.toggle("active", c.dataset.v==="all");
    });
    render();
  });
}

function sortData(arr){
  const sel = document.getElementById("sortSel").value;
  const out = arr.slice();
  const numOf = d => parseInt(String(d.num).replace(/\D/g,""),10) || 0;
  if(sel==="num-desc") out.sort((a,b)=>numOf(b)-numOf(a));
  else if(sel==="bst-desc") out.sort((a,b)=>(b.bst||0)-(a.bst||0));
  else if(sel==="bst-asc") out.sort((a,b)=>(a.bst||0)-(b.bst||0));
  else if(sel==="name-asc") out.sort((a,b)=>a.name.localeCompare(b.name,"vi"));
  else out.sort((a,b)=>numOf(a)-numOf(b));
  return out;
}

function render(){
  const q = document.getElementById("search").value.trim().toLowerCase();
  const grid = document.getElementById("dexGrid");
  let filtered = DATA.filter(d=>{
    if(activeElem!=="all" && !elemMatches(d, activeElem)) return false;
    if(activeRole!=="all" && d.role!==activeRole) return false;
    if(activeStage!=="all" && d.stage!==activeStage) return false;
    if(q && !d.name.toLowerCase().includes(q)) return false;
    return true;
  });
  filtered = sortData(filtered);
  document.getElementById("resultCount").textContent = `${filtered.length} / ${DATA.length} Aniimo`;
  grid.innerHTML = filtered.map(d=>`
    <div class="mon">
      <h4>#${d.num} ${d.name}</h4>
      <div class="meta">
        ${d.stage? `<span class="pill stage-${d.stage.toLowerCase()}">${d.stage}</span>`:""}
        ${elBadgeHTML(d.elem, d.role)}<span class="bst-txt">${d.role}${d.bst?(" · BST "+d.bst):""}</span>
      </div>
      ${d.desc? `<div class="desc">${d.desc}</div>`:""}
      ${d.loc? `<div class="loc">${d.loc}</div>`:""}
      ${d.stats? `<div class="stat-line"><span><b>HP</b> ${d.stats.hp}</span><span><b>ATK</b> ${d.stats.atk}</span><span><b>M.DEF</b> ${d.stats.mdef}</span><span><b>P.DEF</b> ${d.stats.pdef}</span><span><b>BRK</b> ${d.stats.brk}</span><span><b>REGEN</b> ${d.stats.regen}</span></div>`:""}
      ${d.src==="vn"? `<div class="loc">⚠️ Nguồn: fan guide VN — chưa đối chiếu được với Aniidex chính thức</div>`:""}
    </div>
  `).join("");
}

document.getElementById("search").addEventListener("input", render);
document.getElementById("sortSel").addEventListener("change", render);
renderFilters();
render();

document.getElementById("tabs").addEventListener("click", (e)=>{
  const btn = e.target.closest("button");
  if(!btn) return;
  document.querySelectorAll("nav.tabs button").forEach(b=>b.classList.remove("active"));
  btn.classList.add("active");
  document.querySelectorAll("section").forEach(s=>s.classList.remove("active"));
  document.getElementById(btn.dataset.tab).classList.add("active");
  window.scrollTo({top:0,behavior:"instant"});
});
</script>
</body>
</html>
"""

html = html.replace("__DATA__", data_json).replace("__TODAY__", today)
open("index.html","w",encoding="utf-8").write(html)
print("bytes:", len(html))
