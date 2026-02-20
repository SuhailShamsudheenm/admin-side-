package com.example.littlelemon
 
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
 
class MainActivity : ComponentActivity() {
   override fun onCreate(savedInstanceState: Bundle?) {
       super.onCreate(savedInstanceState)
       setContent {
           LittleLemonApp()
       }
   }
}
@Composable
fun LittleLemonApp() {
   MaterialTheme {
       Column {
           Header()
           MenuList(menuItems = sampleMenu)
       }
   }
}
@Composable
fun Header() {
   Box(
       modifier = Modifier
           .fillMaxWidth()
           .padding(16.dp),
       contentAlignment = Alignment.Center
   ) {
       Text(
           text = "Little Lemon Menu",
           fontSize = 24.sp,
           fontWeight = FontWeight.Bold
       )
   }
}
@Composable
fun MenuList(menuItems: List<MenuItem>) {
   LazyColumn(
       modifier = Modifier.padding(16.dp)
   ) {
       items(menuItems) { item ->
           MenuCard(item)
       }
   }
}
@Composable
fun MenuCard(item: MenuItem) {
   Card(
       modifier = Modifier
           .fillMaxWidth()
           .padding(vertical = 8.dp)
   ) {
       Column(modifier = Modifier.padding(16.dp)) {
           Text(text = item.name, fontSize = 20.sp, fontWeight = FontWeight.Bold)
           Text(text = item.description, fontSize = 14.sp)
           Text(text = "$${item.price}", fontWeight = FontWeight.SemiBold)
       }
   }
}
data class MenuItem(
   val name: String,
   val description: String,
   val price: Double
)
val sampleMenu = listOf(
   MenuItem("Greek Salad", "Fresh salad with feta cheese", 12.99),
   MenuItem("Bruschetta", "Grilled bread with tomatoes", 8.99),
   MenuItem("Lemon Dessert", "Traditional lemon cake", 6.99),
   MenuItem("Pasta", "Creamy pasta with herbs", 14.99)
)